package com.second.hand.trading.server.controller;

import java.sql.Timestamp;
import java.util.List;
import java.util.Map;

import org.apache.mahout.cf.taste.common.TasteException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.second.hand.trading.server.enums.ErrorMsg;
import com.second.hand.trading.server.model.OperationModel;
import com.second.hand.trading.server.service.OperationService;
import com.second.hand.trading.server.service.impl.OperationServiceImpl;
import com.second.hand.trading.server.vo.ResultVo;


@RestController
@RequestMapping("operation")
public class OperationController {

    @Autowired
    private OperationService operationService;
    
    @Autowired
    private OperationServiceImpl operationServiceImpl;


     /**
     * 新建操作
     * @param operationModel
     * @return
     */
    @PostMapping("/add")
    public ResultVo createOperation(@RequestBody OperationModel operationModel) {
        System.out.println(operationModel);
        operationModel.setOperationTime(new Timestamp(System.currentTimeMillis()));
        if(operationService.createOperation(operationModel)){
            return ResultVo.success(operationModel);
        }
        return ResultVo.fail(ErrorMsg.OPERATION_CREATE_ERROR);
    }

    @GetMapping("/recommendations/{userid}")
    public List<Long> recommend(@PathVariable Long userid) throws TasteException {
        System.out.println(userid);
        return operationServiceImpl.recommend(userid);
    }

    /**
     * 获取最近7天每天的操作数量之和
     * @param operationType 操作类型
     * @return 每天的操作数量列表
     */
    @GetMapping("/countByDay")
    public ResponseEntity<List<Map<String, Object>>> getRecentOperationsCountByDay(
            @RequestParam("operationType") int operationType) {
        List<Map<String, Object>> operationsCountByDay = operationServiceImpl.getRecentOperationsCountByDay(operationType);
        return ResponseEntity.ok(operationsCountByDay);
    }
    

}
