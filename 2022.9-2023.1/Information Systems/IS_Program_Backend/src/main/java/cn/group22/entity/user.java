package cn.group22.entity;

import lombok.Data;


@Data
public class user {
    private int User_ID;
    private String Password;
    private boolean Admin;
    private int Status;
}
