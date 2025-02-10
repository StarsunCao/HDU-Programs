<template>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="uid"
        label="ID"
        width="100%">
      </el-table-column>
      <el-table-column
        prop="status"
        label="status"
        width="300">
      </el-table-column>
    </el-table>
</template>
<script>
export default {
    data(){
        return{
            tableData:[]
        }
    }
}
</script>