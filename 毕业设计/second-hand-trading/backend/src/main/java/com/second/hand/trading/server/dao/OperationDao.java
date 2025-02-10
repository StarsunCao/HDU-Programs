package com.second.hand.trading.server.dao;

import com.second.hand.trading.server.model.OperationModel;

import java.util.List;
import java.util.Date;
import java.util.Map;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface OperationDao {
    int insert(OperationModel record);
    List<OperationModel> getAllUserPreference();
    List<Map<String, Object>> countOperationsByDay(@Param("operationType") int operationType,
                                                   @Param("startTime") Date startTime);
}
