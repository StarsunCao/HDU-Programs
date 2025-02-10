package cn.group22.tools;

import java.io.File;

public class UploadUtils {
    //静态资源路径
    public final static String IMG_PATH_PREFIX = "static/img";

    public static File getImgDirFile() {
        //dome是项目名
        String fileDirPath = new String("src/main/resources/" + IMG_PATH_PREFIX);

        File fileDir = new File(fileDirPath);
        if (!fileDir.exists()) {

            fileDir.mkdirs();
        }
        return fileDir;
    }

}
