<template>

  <div class="loginBox">

    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="loginForm" auto-complete="on"
      label-position="left" v-if="isShow">

      <el-form-item prop="username" label="ID">

        <el-input id="account" ref="username" v-model="loginForm.username" name="username" type="text" tabindex="1"
          auto-complete="on" />
      </el-form-item>

      <el-form-item prop="password" label="Password">

        <el-input id="password" :key="passwordType" ref="password" v-model="loginForm.password" :type="passwordType"
          name="password" tabindex="2" auto-complete="on" @keyup.enter.native="handleLogin" />
        <span class="show-pwd">

        </span>
      </el-form-item>
      <div style="text-align: center;">
        <el-button id="loginBtn" :loading="loading" type="success" style="width:40%;margin-bottom:30px;margin-top:20px"
          @click.native.prevent="handleLogin" round>Login</el-button>
        <el-button id="registerBtn" :loading="loading" type="info" style="width:40%;margin-bottom:30px;margin-top:20px"
          @click.native.prevent="handleRegister" round>Register</el-button>
      </div>
    </el-form>

    <!-- 注册框 -->
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="loginForm" auto-complete="on"
      label-position="left" v-if="!isShow">

      <el-form-item prop="pwd" label="Password">

        <el-input v-model="loginForm.pwd" ref="pwd" name="pwd" :type="passwordType" />
      </el-form-item>

      <el-form-item prop="cfm" label="Confirm">

        <el-input v-model="loginForm.cfm" ref="cfm" name="cfm" :type="passwordType" />

      </el-form-item>
      <div style="text-align: center;">
        <el-button id="subBtn" :loading="loading" type="success" style="width:40%;margin-bottom:30px;margin-top:20px"
          @click="handleSubmit" round :disabled="(loginForm.pwd === '') || (loginForm.pwd !== loginForm.cfm)">sign up
        </el-button>
        <el-button id="canBtn" :loading="loading" type="info" style="width:40%;margin-bottom:30px;margin-top:20px"
          @click.native.prevent="handleCancel" round>cancel</el-button>
      </div>
    </el-form>
  </div>

</template>

<script src='./login.js'></script>

<style lang="scss">
.info {
  position: fixed;
  bottom: 20px;

  text-align: center;
  color: gainsboro;
}

$bg: #283443;
$light_gray: rgb(0, 0, 0);
$cursor: rgb(0, 0, 0);

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .loginBox .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.loginBox {
  position: relative;
  top: 10%;
  width: 600px;

  .el-input {
    display: inline-block;
    height: 40px;
    width: 70%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      padding: 20px 10px 20px 15px;
      color: $light_gray;
      height: 40px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg: #ffffff;
$dark_gray: #889aa4;
$light_gray: #eee;

.loginBox {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .loginForm {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  // .tips {
  //   font-size: 14px;
  //   color: #fff;
  //   margin-bottom: 10px;

  //   span {
  //     &:first-of-type {
  //       margin-right: 16px;
  //     }
  //   }
  // }

  .svgContainer {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>
