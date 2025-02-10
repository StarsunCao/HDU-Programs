<?php
    function get_name_by_id($id) {
        $xml = simplexml_load_file("persons.xml") or die("Error: Cannot create object");
        foreach ($xml as $element) {
            if ($element['id'] == $id) {
                return $element->name;
            }
        }

        return null;
    }

    //create function that will render html with post.
    function load_posts_by_id($id) { 
        $name = get_name_by_id($id);
        if (empty($name)) {
            return null;
        }

        $xml = simplexml_load_file("posts.xml") or die("Error: Cannot create object");
        //loop for each post in xml
        foreach ($xml as $element) {
            //get posts with author's id 
            if ($element['author'] == $id) {
                //render each post
                echo '<div class="post">';
                echo '<div class="post-header">';
                echo '<span>' . $name .'</span>';
                echo '</div>';
                echo '<div class="post-content">';
                echo $element->body;
                echo '</div></div>';
            }
        }
    }

    function load_person_by_id($id) {
        $xml = simplexml_load_file("persons.xml") or die("Error: Cannot create object");    
        foreach ($xml as $element) {
            if ($element['id'] == $id) {
                $ret = array();
                
                $ret['name'] = $element->name;
                $ret['birthday'] = $element->birthday;
                $ret['city'] = $element->city;
                $ret['about'] = $element->about;
                $ret['gender'] = $element->gender;
                $ret['friendes'] = $element->friendes;

                return $ret;
            }
        }

        return null;
    }

    //check that ID exists.

    if (isset($_GET['id']) && !empty($_GET['id'])) {
        if (empty(get_name_by_id($_GET['id']))) {
            header('Location:404.php');
            die();
        }
    }
    else {
        header('Location:404.php');
        die();
    }

    $personInfo = load_person_by_id($_GET['id']);
        
?>

<!DOCTYPE html>
<html>

<head>
    <title>My personal page</title>
    <link rel="stylesheet" href="style.css" />
</head>

<body>
    <div class="wrapper">
        <div class="topnav">
            <a href="index.php">Home</a>
            <a href="">Friends</a>
            <a href="">Search</a>
            <a href="">Settings</a>
            <a href="">Logout</a>
        </div>

        <div class="personal-info">
            <div class="personal-info-col-left">
                <img src="http://mms2.baidu.com/it/u=1171179783,109636153&fm=253&app=138&f=JPEG&fmt=auto&q=75?w=432&h=576" />
            </div>
            <div class="personal-info-col-right">
                <h2><?= $personInfo['name'] ?></h2>
                <hr />
                <div class="personal-info-item">
                    <div class="personal-info-item-label">City:</div>
                    <div class="personal-info-item-value"><?= $personInfo['city'] ?></div>
                </div>
                <div class="personal-info-item">
                    <div class="personal-info-item-label">Birthday:</div>
                    <div class="personal-info-item-value"><?= $personInfo['birthday'] ?></div>
                </div>
                <div class="personal-info-item">
                    <div class="personal-info-item-label">Friends:</div>
                    <div class="personal-info-item-value"><?= $friends ?></div>
                </div>
                <div class="personal-info-item">
                    <div class="personal-info-item-label">About:</div>
                    <div class="personal-info-item-value"><?= $personInfo['about'] ?></div>
                </div>
            </div>
        </div>

        <div class="post-container">
           <?php 
            if (isset($_GET['id']) && !empty($_GET['id'])) {
                //call load_posts function to render all posts.
                load_posts_by_id($_GET['id']);
            }
            else {  
                header('Location:404.php');
                die();
            }
           ?>            
        </div>
    </div>
</body>
</html>