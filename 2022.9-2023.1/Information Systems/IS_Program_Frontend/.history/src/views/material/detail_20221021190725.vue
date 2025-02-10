<template>
    <div>

        <div class="description" style="margin-top:50px">
            <h1>Description:{{data1.description}}</h1>
        </div>
        <div class="goBack" style="margin-top:70px">
            <el-image style="width: 420px; height: 320px;" :src="img_path" />
            <h1>address:{{data1.address}}</h1>
            <h1>price:{{data1.price}}</h1>
            <h1>email:{{data1.email}}</h1>
        </div>
        <el-button type="success" round class="goBack" @click="goBack" style="margin-top:20px">
            Back
        </el-button>
    </div>

</template>

<script>

export default {
    data() {
        return {
            name: "detail",
            data1: [],
            img_path: ''
        }
    },

    methods: {
        goBack() {
            this.$router.push('/material');
        },
        getDetailRecords() {
            this.req({
                url: "/apartment/findByApartmentID",
                data: {
                    Apartment_ID: localStorage.getItem('APid')
                },
                method: "POST"
            }).then(res => {
                console.log(res);
                this.data1 = res.data[0]
                console.log(this.data1);
                this.img_path = 'http://192.168.31.73:8080/images/' + this.data1.picture
                console.log(this.img_path)
            })
        }
    },
    created() {
        this.getDetailRecords()
    },

}
</script>
<style>
.goBack {
    position: absolute;
    left: 20%;
}

.description {
    position: absolute;
    left: 60%;
    text-align: left;
    word-break: break-word;
}
</style>