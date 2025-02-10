   function gettime(){
    $.ajax({
url:"/time",
        timeout:10000,
        success:function (data){
        $("#tim").html(data)
        },error:function (xhr,type,errorThrown){

        }
    });
}
function getdata(){
         $.ajax({
url:"/data",
        timeout:10000,
        success:function (data){
            $("#num").text(data.num)
            $("#name").text(data.name)
            $("#volume").text(data.volume)
            $("#prise").text(data.prise)
            $('#picture').attr("src",data.picture);
        },error:function (xhr,type,errorThrown){

        }
    });

}
//  function get_map_data(){
//     $.ajax({
// url:"/map",
//         timeout:10000,
//         success:function (data){
//        map.mydata = data
//         },error:function (xhr,type,errorThrown){
//
//         }
//     });
// }
