export default {
    name: "Login",
    data() {
        const uname = (rule, value, callback) => {
            if (value.length == 0) {
                callback(new Error("please input the correct ID"));
            } else {
                callback();
            }
        };
        const upassword = (rule, value, callback) => {
            if (value.length == 0) {
                callback(new Error("please input the correct password"));
            } else {
                callback();
            }
        };
        const rpwd = (rule, value, callback) => {
            if (value.length == 0) {
                callback(new Error("please input password"));
            } else {
                callback();
            }
        };
        const rcfm = (rule, value, callback) => {
            if (value !== this.loginForm.pwd) {
                callback(new Error("please input the same password"));
            } else {
                callback();
            }
        };
        return {
            loginForm: {
                username: '',
                password: '',
                pwd: '',
                cfm: '',

            },
            loginRules: {
                username: [
                    { required: true, trigger: "blur", validator: uname }
                ],
                password: [
                    { required: true, trigger: "blur", validator: upassword }
                ],
                pwd: [
                    { required: true, trigger: "blur", validator: rpwd }
                ],
                cfm: [
                    { required: true, trigger: "blur", validator: rcfm }
                ]
            },
            loading: false,
            passwordType: "password",
            redirect: undefined,
            isShow: true
        };
    },
    watch: {
        $route: {
            handler: function(route) {
                this.redirect = route.query && route.query.redirect;
            },
            immediate: true
        }
    },
    methods: {
        // showPwd() {
        //     if (this.passwordType === "password") {
        //         this.passwordType = "";
        //     } else {
        //         this.passwordType = "password";
        //     }
        //     this.$nextTick(() => {
        //         this.$refs.password.focus();
        //     });
        // },
        handleLogin() {
            // // 开发模式下设置默认登录
            // localStorage.setItem("hasLogin", true);
            // this.$router.push({ path: "/" });

            // let that = this;
            // this.loading = true;
            // //数据格式验证
            // this.$refs.loginForm.validate(valid => {
            //     if (valid) {
            //         this.loginFlag = true
            //     } else {
            //         console.log("验证失败");
            //     }
            // });
            // // 开发模式下设置取消登录请求
            // // return 0;
            // // 发送登录请求
            this.req({
                url: "/user/findByUserID",
                data: {
                    User_ID: this.loginForm.username,
                },
                method: "POST"
            }).then(
                res => {
                    console.log("res :", res);
                    if (res.data.length == 0) {
                        alert('userID does not exist')
                    } else if (res.data[0].password == this.loginForm.password) {
                        localStorage.setItem('hasLogin', true)
                        localStorage.setItem('userID', this.loginForm.username)
                        localStorage.setItem('admin', res.data[0].admin)
                        this.$router.push({ path: this.redirect })

                    } else {
                        alert('wrong password')
                    }
                    // if (res.data.data) {
                    //     localStorage.setItem('hasLogin', true)
                    //     localStorage.setItem('userInfo', JSON.stringify(res.data.data))
                    //     if (this.redirect) {
                    //         this.$router.push({ path: this.redirect })
                    //     } else {
                    //         this.$router.push({ path: '/' })
                    //     }
                    // } else {
                    //     console.log("login err :", res);
                    //     alert(res.data.msg)
                    //     this.passwordError = true
                    //     this.loading = false
                    //     this.$router.push({ path: '/login' })
                    // }
                },
            );
        },
        handleRegister() {
            this.isShow = !this.isShow
            this.loginForm.pwd = ''
            this.loginForm.cfm = ''
        },
        handleSubmit() {
            this.isShow = !this.isShow
            this.req({
                url: "/user/addUser",
                data: {
                    Password: this.loginForm.pwd
                },
                method: "PUT"
            }).then(res => {
                this.loginForm.username = res.data.returnObj.userID
                this.loginForm.password = ''
            })
        },
        handleCancel() {
            this.isShow = !this.isShow
            this.loginForm.pwd = ''
            this.loginForm.cfm = ''
        }
    },
    mounted() {
        localStorage.setItem('host', window.location.host)
    }
};