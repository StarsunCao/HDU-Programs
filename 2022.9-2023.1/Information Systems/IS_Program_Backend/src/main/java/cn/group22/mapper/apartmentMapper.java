package cn.group22.mapper;

import cn.group22.entity.apartment;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
@Repository
public interface apartmentMapper {
    public List<apartment> findByApartmentID(@Param("Apartment_ID") int Apartment_ID);
    public void addApartment(
            @Param("Apartment_ID") int Apartment_ID,
            @Param("Address") String Address,
            @Param("Description") String Description,
            @Param("Picture") String Picture,
            @Param("User_ID") int User_ID,
            @Param("Price") int Price,
            @Param("Email") String Email);
    public void updateApartment(
            @Param("Apartment_ID") int Apartment_ID,
            @Param("Address") String Address,
            @Param("Description") String Description,
            @Param("Picture") String Picture,
            @Param("Price") int Price,
            @Param("Email") String Email);
    public void delApartment(@Param("Apartment_ID") int Apartment_ID);

    public List<apartment> searchApartment(@Param("Keywords") String Keywords);

    @Select("select * from apartment")
    public List<apartment> findAll();
}
