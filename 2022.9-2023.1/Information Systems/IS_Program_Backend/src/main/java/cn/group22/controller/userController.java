package cn.group22.controller;

import cn.group22.entity.user;
import cn.group22.service.userService;
import cn.group22.tools.ObjectRESTResult;
import io.swagger.annotations.Api;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import sun.security.util.Password;

import java.io.*;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

@CrossOrigin
@RestController
@Slf4j
@RequestMapping(value = "/user")
@Api(value = "userApi", tags = "用户接口")
public class userController {
    @Autowired
    private userService uServ;

    @RequestMapping(value = "/findAllU",method = RequestMethod.GET)
    public List<user> findAll() {
        return uServ.findAll();
    };

    @RequestMapping(value = "/findByUserID", method = RequestMethod.POST)
    public List<user> findByUserID(@RequestBody Map<String, String> maps) {
        int myID = Integer.parseInt(maps.get("User_ID"));
        return uServ.findByUserID(myID);
    };

    @PutMapping(value = "/addUser")
    public ObjectRESTResult addUser(@RequestBody Map<String, String> maps) throws IOException {
        String path = "src/main/resources/id/uid.txt";

        int uID;
        File f = new File(path);
        Scanner scan = new Scanner(f);
        uID =scan.nextInt();
        uID++;

        FileWriter writer = new FileWriter(path);
        writer.write(Integer.toString(uID));
        writer.flush();
        writer.close();

        String Password = maps.get("Password");
        uServ.addUser(uID, Password, false);

        Map<String, Object> emp = new HashMap<>();
        emp.put("userID", uID);
        ObjectRESTResult restResult = new ObjectRESTResult();
        restResult.setReturnObj(emp);

        return restResult;
    };

    @PutMapping(value = "/updatePassword")
    public void updatePassword(@RequestBody Map<String, String> maps){
        int uID = Integer.parseInt(maps.get("User_ID"));
        uServ.updatePassword(uID,maps.get("Password"));
    };

    @PutMapping(value = "/changeStatus")
    public void changeStatus(@RequestBody Map<String, String> maps){
        int uID = Integer.parseInt(maps.get("User_ID"));
        int status = Integer.parseInt(maps.get("Status"));
        uServ.changeStatus(uID,status);
    }
}
