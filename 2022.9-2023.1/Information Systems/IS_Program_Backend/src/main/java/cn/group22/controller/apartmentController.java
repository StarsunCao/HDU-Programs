package cn.group22.controller;

import cn.group22.entity.apartment;
import cn.group22.service.apartmentService;
import cn.group22.tools.ObjectRESTResult;
import cn.group22.tools.UploadUtils;
import io.swagger.annotations.Api;
import lombok.extern.slf4j.Slf4j;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import javax.sql.rowset.serial.SerialException;
import java.io.*;
import java.sql.SQLException;
import java.util.*;

@Resource
@CrossOrigin
@RestController
@Slf4j
@RequestMapping(value = "/apartment")
@Api(value = "apartmentApi", tags = "房子接口")
public class apartmentController {
    @Autowired
    private apartmentService aServ;

    @RequestMapping(value = "/findAllA", method = RequestMethod.GET)
    public List<apartment> findAll() {
        return aServ.findAll();
    }

    @RequestMapping(value = "/findByApartmentID", method = RequestMethod.POST)
    public List<apartment> findByApartmentID(@RequestBody Map<String, String> maps) {
        int aID = Integer.valueOf(maps.get("Apartment_ID"));
        return aServ.findByApartmentID(aID);
    }

    @RequestMapping(value = "/searchApartment", method = RequestMethod.POST)
    public List<apartment> searchApartment(@RequestBody Map<String,String> maps){
        return aServ.searchApartment(maps.get("Keywords"));
    }

    @PutMapping(value = "/addApartment")
    public void addApartment(@RequestBody Map<String, String> maps) throws SerialException, SQLException, SQLException, IOException {
        String path = "src/main/resources/id/aid.txt";

        int aID;
        File f = new File(path);
        Scanner scan = new Scanner(f);
        aID =scan.nextInt();
        aID++;

        FileWriter writer = new FileWriter(path);
        writer.write(Integer.toString(aID));
        writer.flush();
        writer.close();

        int uID;
        uID = Integer.parseInt(maps.get("User_ID"));
        int Price = Integer.parseInt(maps.get("Price"));
        aServ.addApartment(aID, maps.get("Address"), maps.get("Description"), maps.get("Picture"), uID,Price,maps.get("Email"));

    }

    @PutMapping(value = "/updateApartment")
    public void updateApartment(@RequestBody Map<String, String> maps) throws SerialException, SQLException{
        int aID = Integer.parseInt(maps.get("Apartment_ID"));
        int Price = Integer.parseInt(maps.get("Price"));
        aServ.updateApartment(aID,maps.get("Address"), maps.get("Description"), maps.get("Picture"), Price,maps.get("Email"));
    };

    @DeleteMapping(value = "/delApartment")
    public void delApartment(@RequestBody Map<String,String> maps){
        System.out.println("controller begin");
        int aID = Integer.valueOf(maps.get("Apartment_ID"));
        aServ.delApartment(aID);
        System.out.println("controller over");
    }

    @ResponseBody
    @RequestMapping(value = "/upload" )
    public ObjectRESTResult upload(@RequestParam("file") MultipartFile imgFile, HttpServletRequest request, HttpSession session) {

        ObjectRESTResult restResult = new ObjectRESTResult();

//            if (imgFile.isEmpty()) {
//                logger.error("上传失败，请选择文件");
//                restResult.setMsg("上传失败，请选择文件");
//                return restResult;
//            }

        // 生成唯一文件名
        String uuid = UUID.randomUUID().toString().trim();
        String filename = imgFile.getOriginalFilename();
        int index = filename.indexOf(".");
        String fileNames = uuid + filename.substring(index);

        // 调用UploadUtils工具类将图片存放到服务器上
        File fileDir = UploadUtils.getImgDirFile();

        try {
            // 构建真实的文件路径
            File newFile = new File(fileDir.getAbsolutePath() + File.separator + fileNames);
            System.out.println(newFile.getAbsolutePath());

            imgFile.transferTo(newFile);

        } catch (IOException e) {
            e.printStackTrace();
        }
        Map<String, Object> emp = new HashMap<>();
        emp.put("fileName", fileNames);
        //返回图片名称
        restResult.setReturnObj(emp);
        return restResult;
    }
}
