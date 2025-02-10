<template>
  <div>

    <el-form label-width="auto" style="max-width: 600px" size="large" class="addForm demo-dynamic"
      :model="dynamicValidateForm" ref="dynamicValidateForm">
      <h1 style="font-size: 40px">Edit Information</h1>
      <el-form-item label="Address">
        <el-input v-model="Address" />
      </el-form-item>
      <el-form-item label="Price">
        <el-input v-model="Price" type="number" />

      </el-form-item>
      <el-form-item label="Email" prop="Email" :rules="[
        { type: 'email', message: 'please input a correct email', trigger: ['blur', 'change'] }
      ]">
        <el-input v-model="dynamicValidateForm.Email" />
      </el-form-item>

      <el-form-item label="Description">
        <el-input v-model="Description" :rows="3" type="textarea" :autosize="{ minRows: 3, maxRows: 6 }" />
      </el-form-item>
      <el-upload class="upload-demo" drag action="localhost:8080/apartment/upload" multiple
        :on-success="handle_success">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">drop one picture here <em>upload</em></div>

      </el-upload>
    </el-form>
    <!--  -->
    <div>
      <el-button type="info" round class="cancel" @click="cancel">
        cancel</el-button>

      <el-button type="success" round class="submit"
        :disabled="!(Address&&Price&&Description&&dynamicValidateForm.Email&&Picture)" @click="submit">
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
      }
    };
  },


  methods: {
    submit() {
      this.$refs.dynamicValidateForm.validate((valid) => {
        if (valid) {
          this.req({
            url: "/apartment/updateApartment",
            data: {
              Address: this.Address,
              Price: this.Price,
              Description: this.Description,
              Email: this.dynamicValidateForm.Email,
              Picture: this.Picture,
              Apartment_ID: localStorage.getItem('APid')

            },
            method: "PUT"
          }).then((res) => {
            console.log('res:', res)

          })
          const h = this.$createElement;

          this.$notify({
            title: 'Congratulations！',
            message: h('i', { style: 'color: teal' }, 'your advertisement was changed successfully')
          });
          this.$router.push('/material');
        } else {
          alert('error submit!!');
          return false;
        }
      });
    },
    cancel() {
      this.$router.push('/material');
    },
    handle_success(res) {
      console.log(res);
      this.Picture = res.returnObj.fileName
      console.log(this.Picture);
    },
    getDetailRecords() {
      this.req({
        url: "/apartment/findByApartmentID",
        data: {
          Apartment_ID: localStorage.getItem('APid')
        },
        method: "POST"
      }).then(res => {
        this.Address = res.data[0].address
        this.Price = res.data[0].price
        this.Description = res.data[0].description
        this.dynamicValidateForm.Email = res.data[0].email
        this.Picture = res.data[0].picture
      })
    }
  },
  created() {
    this.getDetailRecords()
  },
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
  left: 47%;
  top: 90%;
  width: 100px;
}

.cancel {
  position: absolute;
  left: 35%;
  top: 90%;
  width: 100px;
}
</style>