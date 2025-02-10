package cn.group22.tools;

public class ObjectRESTResult {
    protected int statusCode;
    protected Object returnObj;
    protected String msg;

    public ObjectRESTResult() {
    }

    public String getMsg() {
        return this.msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    public int getStatusCode() {
        return this.statusCode;
    }

    public void setStatusCode(int statusCode) {
        this.statusCode = statusCode;
    }

    public Object getReturnObj() {
        return this.returnObj;
    }

    public void setReturnObj(Object returnObj) {
        this.returnObj = returnObj;
    }

}
