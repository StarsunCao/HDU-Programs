package cn.group22.mapper;

import cn.group22.entity.user;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
@Repository
public interface userMapper {
    public List<user> findByUserID(@Param("User_ID") int User_ID);
    public void addUser(@Param("User_ID") int User_ID,@Param("Password") String Password,@Param("Admim") boolean Admim);
    public void updatePassword(@Param("User_ID") int User_ID,@Param("Password") String Password);

    public void changeStatus(@Param("User_ID") int User_ID, @Param("Status") int Status);

    @Select("select * from user")
    public List<user> findAll();
}
