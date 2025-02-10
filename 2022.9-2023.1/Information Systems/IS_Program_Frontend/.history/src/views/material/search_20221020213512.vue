<template>
  <div class="mt-4">
    <el-input v-model="input1" class="w-50 m-2" placeholder="Input keyword" input-style="width:500px;height:40px">
      <template #append>
        <el-button @click="search" icon="el-icon-search"></el-button>
      </template>
    </el-input>
    <el-table :data="data1" style="width: 100%;max-height:80% ;" >
      <el-table-column prop="apartment_ID" label="Apartment_ID" width="160">

      </el-table-column>
      <el-table-column prop="picture" label="picture" width="300px">
        <template v-slot="scope">
          <el-image :src="'localhost:8080/images/'+scope.row.picture" style="width:210px;height:150px">
          </el-image>
        </template>
      </el-table-column>
      <el-table-column prop="address" label="address" width="180"></el-table-column>
      <el-table-column prop="description" label="description" width="400"></el-table-column>
      <el-table-column prop="price" label="price" width="150"></el-table-column>

      <el-table-column label="operation" width="300px">
        <div slot-scope="scope">
        <el-button type="success"
         circle  @click="rowClick(scope.row.apartment_ID)" 
         icon="el-icon-tickets"></el-button>
        <el-button type="success" 
        circle @click="edit(scope.row.apartment_ID)" icon="el-icon-edit" v-if="(uid == scope.row.user_ID)||(JSON.parse(admin) == true)"></el-button>
        <el-button type="info " circle @click="del(scope.row.apartment_ID)" icon="el-icon-delete" v-if="(uid == scope.row.user_ID)||(JSON.parse(admin) == true)"></el-button>
        </div>
      </el-table-column>
    </el-table>

    
  </div>
</template>
<script>

export default {
  data() {
    return {
      name: "search",
      input1: '',
      data1: [],
      uid:'',
      admin: false,
    }
  },

  methods: {
    rowClick(id) {
      this.$router.push('/detail');
      localStorage.setItem('APid',id)
      // this.data1.map(item => {
      //   let flag = (this.uid == item.user_ID)
      //   console.log(this.admin||flag)
      // })
    },
    edit(id) {
      this.$router.push('/editInfo');
      localStorage.setItem('APid',id)
      
      
    },
    del(id) {
      
      this.req({
        url:"/apartment/delApartment",
        data:{
          Apartment_ID:id
        },
        method:"DELETE"
      }).then((res)=>{
        console.log(res)
        this.getApartmentList()
      })
    },
    getApartmentList() {
      this.req({
        url: "/apartment/findAllA",
        data: {},
        method: "GET"
      }).then((res) => {
        this.uid=localStorage.getItem('userID')
        this.admin=localStorage.getItem('admin')
        this.data1 = res.data
      })
    },
    search(){
      this.req({
        url: "/apartment/searchApartment",
        data:{
          Keywords:this.input1
        },
        method:"POST"
      }).then((res)=>{
        this.data1 = res.data
      })
    }
  },
  created() {
    this.getApartmentList()

  },
}
</script>
