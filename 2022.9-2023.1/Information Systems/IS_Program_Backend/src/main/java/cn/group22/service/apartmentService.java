package cn.group22.service;

import cn.group22.entity.apartment;
import cn.group22.mapper.apartmentMapper;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

@Service

public class apartmentService {
    @Resource
    private apartmentMapper aMapper;

    public List<apartment> findByApartmentID(int Apartment_ID) {
        return aMapper.findByApartmentID(Apartment_ID);
    }

    public void addApartment(int Apartment_ID, String Address, String Description,String Picture, int User_ID, int Price, String Email) {
        aMapper.addApartment(Apartment_ID, Address, Description,Picture,User_ID,Price,Email);
    }

    public void updateApartment(int Apartment_ID, String Address, String Description, String Picture,int Price, String Email){
        aMapper.updateApartment(Apartment_ID, Address, Description,Picture,Price,Email);
    }

    public List<apartment> findAll() {
        return aMapper.findAll();
    }

    public void delApartment(@Param("Apartment_ID") int Apartment_ID){
        aMapper.delApartment(Apartment_ID);
    }

    public List<apartment> searchApartment(String Keywords){return aMapper.searchApartment(Keywords);}
}
