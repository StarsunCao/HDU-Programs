package cn.group22.service;

import cn.group22.entity.user;
import cn.group22.mapper.userMapper;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

@Service

public class userService {
    @Resource
    private userMapper uMapper;

    public List<user> findByUserID(int User_ID) {
        return uMapper.findByUserID(User_ID);
    }

    public void addUser(int User_ID, String Password, boolean Admin) {
        uMapper.addUser(User_ID, Password, Admin);
    }

    public void updatePassword(int User_ID, String Password){
        uMapper.updatePassword(User_ID, Password);
    }

    public void changeStatus(int User_ID, int Status){uMapper.changeStatus(User_ID,Status);}

    public List<user> findAll() {
        return uMapper.findAll();
    }

}
