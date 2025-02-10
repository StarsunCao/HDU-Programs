<template>
  <div>

    <el-form label-width="auto" style="max-width: 600px" size="large" class="addForm demo-dynamic"
      :model="dynamicValidateForm" ref="dynamicValidateForm">
      <h1 style="font-size: 40px">Add New Apartment</h1>
      <el-form-item label="Address">
        <el-input v-model="Address" />
      </el-form-item>
      <el-form-item label="Price">
        <el-input v-model="Price" type="number" />

      </el-form-item>
      <el-form-item label="Email" prop="Email" :rules="[
        
        { type: 'email', message: 'input a correct email!', trigger: ['blur', 'change'] }
      ]">
        <el-input v-model="dynamicValidateForm.Email" />
      </el-form-item>

      <el-form-item label="Description">
        <el-input v-model="Description" :rows="3" type="textarea" :autosize="{ minRows: 3, maxRows: 6 }" />
      </el-form-item>
      <el-upload class="upload-demo" drag action="http://192.168.31.73:8080/apartment/upload" multiple
        :on-success="handle_success">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">drop one picture here <em>upload</em></div>

      </el-upload>
    </el-form>
    <!--  -->
    <div>
      <el-button type="success" round class="submit"
        :disabled="!(Address&&Price&&Description&&dynamicValidateForm.Email&&Picture)"
        @click="submit(dynamicValidateForm)">
        submit</el-button>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      Address: '',
      Price: '',
      Description: '',
      Picture: '',
      dynamicValidateForm: {
        Email: ''
      },
      rules: true
    };
  },


  methods: {
    submit() {
      this.$refs.dynamicValidateForm.validate((valid) => {
        if (valid) {
          this.req({
            url: "/apartment/addApartment",
            data: {
              Address: this.Address,
              Price: this.Price,
              Description: this.Description,
              Email: this.dynamicValidateForm.Email,
              Picture: this.Picture,
              User_ID: localStorage.getItem('userID')
            },
            method: "PUT"
          }).then((res) => {
            console.log('res:', res)

          })
          const h = this.$createElement;

          this.$notify({
            title: 'Congratulations！',
            message: h('i', { style: 'color: teal' }, 'your advertisement was submitted successfully')
          });
          this.$router.push('/material');
        } else {
          alert('error submit!!');
          return false;
        }
      });
    },
    handle_success(res) {
      console.log(res);
      this.Picture = res.returnObj.fileName
      console.log(this.Picture);
    }
  }
}
</script>
<style>
.addForm {
  position: absolute;
  left: 30%;
  width: 500px;
  text-align: right;

}

.submit {

  position: absolute;
  left: 40%;
  top: 90%;
  width: 100px;
}
</style>