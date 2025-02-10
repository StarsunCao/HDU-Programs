package com.second.hand.trading.server.service.impl;

import com.second.hand.trading.server.dao.OperationDao;
import com.second.hand.trading.server.service.OperationService;
import com.second.hand.trading.server.model.OperationModel;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.impl.common.FastByIDMap;
import org.apache.mahout.cf.taste.impl.model.GenericDataModel;
import org.apache.mahout.cf.taste.impl.model.GenericPreference;
import org.apache.mahout.cf.taste.impl.model.GenericUserPreferenceArray;
import org.apache.mahout.cf.taste.impl.neighborhood.NearestNUserNeighborhood;
import org.apache.mahout.cf.taste.impl.recommender.GenericUserBasedRecommender;
import org.apache.mahout.cf.taste.impl.similarity.UncenteredCosineSimilarity;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.cf.taste.model.PreferenceArray;
import org.apache.mahout.cf.taste.neighborhood.UserNeighborhood;
import org.apache.mahout.cf.taste.recommender.RecommendedItem;
import org.apache.mahout.cf.taste.recommender.Recommender;
import org.apache.mahout.cf.taste.similarity.UserSimilarity;
import org.springframework.stereotype.Service;

import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Map;
import java.util.*;

import javax.annotation.Resource;

@Service
public class OperationServiceImpl implements OperationService{

    @Resource
    private OperationDao operationDao;

    /**
     *新增
     * @param operationModel
     * @return
     */
    public boolean createOperation(OperationModel operationModel){
        return operationDao.insert(operationModel) == 1;
    }

    public List<Long> recommend(Long userId) throws TasteException {
        List<OperationModel> userList = operationDao.getAllUserPreference();
        if (userList == null || userList.isEmpty()) {
        // 处理空列表的情况，可能是返回空列表或抛出异常
        return Collections.emptyList();
        }
        // System.out.println("userList:"+userList);
        //创建数据模型
        DataModel dataModel = this.createDataModel(userList);
        //获取用户相似程度
        UserSimilarity similarity = new UncenteredCosineSimilarity(dataModel);
        //获取用户邻居
        UserNeighborhood userNeighborhood = new NearestNUserNeighborhood(2, similarity, dataModel);
        //构建推荐器
        Recommender recommender = new GenericUserBasedRecommender(dataModel, userNeighborhood, similarity);
        //推荐2个
        List<RecommendedItem> recommendedItems = recommender.recommend(userId, 8);
        List<Long> itemIds = recommendedItems.stream().map(RecommendedItem::getItemID).collect(Collectors.toList());
        // System.out.println("dataModel:"+dataModel);
        // System.out.println("similarity:"+similarity);
        // System.out.println("userNeighborhood:"+userNeighborhood);
        // System.out.println("recommender:"+recommender);
        // System.out.println("recommendedItems:"+recommendedItems);
        // System.out.println("itemIds:"+itemIds);
        return itemIds;
    }
    private DataModel createDataModel(List<OperationModel> operationModels) {
        FastByIDMap<PreferenceArray> fastByIdMap = new FastByIDMap<>();
        Map<Long, List<OperationModel>> map = operationModels.stream().collect(Collectors.groupingBy(OperationModel::getUserId));
        Collection<List<OperationModel>> list = map.values();
        for(List<OperationModel> userPreferences : list){
            GenericPreference[] array = new GenericPreference[userPreferences.size()];
            for(int i = 0; i < userPreferences.size(); i++){
                OperationModel userPreference = userPreferences.get(i);
                GenericPreference item = new GenericPreference(userPreference.getUserId(), userPreference.getIdleId(), userPreference.getValue());
                array[i] = item;
            }
            fastByIdMap.put(array[0].getUserID(), new GenericUserPreferenceArray(Arrays.asList(array)));
        }
        return new GenericDataModel(fastByIdMap);
    }

    /**
     * 获取最近7天每天的操作数量之和
     * @param operationType 操作类型
     * @return 每天的操作数量列表
     */
    public List<Map<String, Object>> getRecentOperationsCountByDay(int operationType) {
        // 创建Calendar实例来计算7天前的日期
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.DAY_OF_MONTH, -7);
        Date sevenDaysAgo = calendar.getTime();

        // 调用Dao层方法获取数据
        return operationDao.countOperationsByDay(operationType, sevenDaysAgo);
    }

}
