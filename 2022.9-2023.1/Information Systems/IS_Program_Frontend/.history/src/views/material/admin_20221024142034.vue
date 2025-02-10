<template
v-if="JSON.parse(admin) == true">
    
    <el-table
      :data="tableData"
      style="width: 100%"
      >
      <el-table-column
        prop="uid"
        label="ID"
        width="1000">
      </el-table-column>
      <el-table-column
        prop="status"
        label="status"
        width="300">
      </el-table-column>
    </el-table>
    
</template>
<template
v-if="JSON.parse(admin) == false">
    <span>you cannot admin</span>
</template>
<script>
export default {
    data() {
        return {
            tableData: [],
            admin: localStorage.getItem('admin'),
        }
    },
    methods: {
        findUsers() {

        }
    },
}
</script>