<template>
    <div>
        <el-table :data="tableData" style="width: 100%" v-if="JSON.parse(admin) == true">
            <el-table-column prop="user_ID" label="ID" width="1000"> </el-table-column>
            <el-table-column prop="status" label="status" width="300">
                <template v-slot="scope">
                    <el-switch v-model="scope.row.status" active-color="#13ce66" inactive-color="#ff4949"
                        @change="change(scope.row.user_ID,scope.row.status)">
                    </el-switch>
                </template>
            </el-table-column>
        </el-table>
        <h1 class="warn" v-if="JSON.parse(admin) == false">you cannot admin</h1>
    </div>
</template>
<script>
export default {
    data() {
        return {
            tableData: [],
            admin: localStorage.getItem("admin"),
        };
    },
    methods: {
        findUsers() {
            this.req({
                url: "/user/findAllU",
                data: {},
                method: "GET",
            }).then((res) => {
                this.tableData = res.data;
                console.log(res)
            });
        },
        change(id,status) {
            this.req({
                url:"/user/changeStatus",
                data:{
                    User_ID:id,
                    Status:!status
                },
                methods:"PUT"
            })
        }
    },
    created() {
        this.findUsers()
    }
};
</script>
<style>
.warn {
    position: absolute;
    left: 40%;
}
</style>