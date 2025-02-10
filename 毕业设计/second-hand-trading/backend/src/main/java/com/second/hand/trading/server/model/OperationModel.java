package com.second.hand.trading.server.model;

import java.io.Serializable;
import java.util.Date;

public class OperationModel implements Serializable{

    //自增主键
    private Long id;

    //用户id
    private Long userId;

    //商品id
    private Long idleId;

    //操作类型
    private int type;

    //操作时间
    private Date operationTime;

    //分数
    private Integer value;

    public Long getId(){
        return id;
    }

    public void setId(Long id){
        this.id = id;
    }

    public Long getUserId(){
        return userId;
    }

    public void setUserId(Long userId){
        this.userId = userId;
    }

    public Long getIdleId(){
        return idleId;
    }

    public void setIdleId(Long idleId){
        this.idleId = idleId;
    }

    public int getType(){
        return type;
    }

    public void setType(int type){
        this.type = type;
    }

    public Date getOperationTime(){
        return operationTime;
    }

    public void setOperationTime(Date operationTime){
        this.operationTime = operationTime;
    }

    public Integer getValue(){
        return value;
    }

    public void setValue(Integer value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "Operation{" +
                "id=" + id +
                ", userId=" + userId +
                ", idleId=" + idleId +
                ", operationType=" + type +
                ", value=" + value +
                '}';
    }
}
