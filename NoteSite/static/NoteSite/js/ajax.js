$("#filter").change(function (e) {
    e.preventDefault();

    $.ajax({
        type:'GET',
        url:'/my_notes/ajax/',
        data:{
            'title':$('#id_title').val(),
            'date':$('#id_date').val(),
            'category':$('#id_category').val(),
            'favorite':$('#id_favorite').val(),
            // 'order_by':$('')
        },
        dataType: 'html',
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        success:filterSuccess,
    });

});
function filterSuccess(data)
{
    $('.table').html(data)
}
// $("#submits").click(function (e) {
//     e.preventDefault();
//
//     $.ajax({
//         type: 'GET',
//         url:'/my_notes/ajax/',
//         data:{
//             'order_by':$('href').val()
//         },
//         dataType: 'html',
//         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         success:sortSuccess,
//     });
// });
// function sortSuccess(data)
// {
//     $('.table').html(data)
// }
//
// $("#filter").change(function (e) {
//     e.preventDefault();
//
//     $.ajax({
//         type:'GET',
//         url:'/my_notes/ajax/',
//         data:{
//             'title':$('#id_title').val(),
//             'date':$('#id_date').val(),
//             'category':$('#id_category').val(),
//             'favorite':$('#id_favorite').val()
//         },
//         dataType: 'html',
//         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         success:filterSuccess,
//     });
//
// });
// function filterSuccess(data)
// {
//     $('.table').html(data)
// }
$("#register_form").on("submit", function (event) {
    event.preventDefault();
    console.log("Форма отправлена!");
    create_user();
});
//
// $('#id_username').change(function () {
// var username = $(this).val();
//
// $.ajax({
//     url:'/register/',
//     data:{
//         'username':username
//     },
//     dataType:'json',
//     success: function (data) {
//         if (data.is_taken){
//             alert("A user with this username already exists.")
//         }
//     }
// });
// });