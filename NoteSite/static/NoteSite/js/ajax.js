$(document).ready(function () {
    $(document).on("submit","#id_register_form", function (e) {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: "/register/",
            data: {
                username:$('#id_username').val(),
                password1:$('#id_password1').val(),
                password2:$('#id_password2').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            dataType: "html",
            success: function () {
                alert("Created new account! Now you can sign in!")
            },
        });
    });

    // $(document).on("submit","#id_login_form", function (e) {
    //     e.preventDefault();
    //
    //     $.ajax({
    //         type: "POST",
    //         url: "/login/",
    //         data: {
    //             username:$('#id_username').val(),
    //             password:$('#id_password').val(),
    //             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    //         },
    //         dataType: "html",
    //         success: function () {
    //             alert("Successful sign in!")
    //         },
    //     });
    // });

    $(document).on("click","#id_sign_up",function (e) {
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: "/register/",
            data: {},
            dataType: "html",
            success: clickSuccess,
        });
    });

    $(document).on("click","#id_sign_in",function (e) {
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: "/login/",
            data: {},
            dataType: "html",
            success: clickSuccess,
        });
    });

    $(document).on("click","#id_home",function (e) {
        console.log("A");
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: "/home/",
            data: {},
            dataType: "html",
            success: clickSuccess,
        });
    });

    $(document).on("click","#id_filter", function (e) {
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: "/my_notes/",
            data: {},
            dataType: "html",
            success: clickSuccess,
        });
    });

    $(document).on("click","#id_new_note", function (e) {
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: "/my_notes/new/",
            data: {},
            dataType: "html",
            success: clickSuccess,
        });
    });

    $(document).on("submit","#id_new_note_form", function (e) {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: "/my_notes/new/",
            data: {
                title:$('#id_title').val(),
                text:$('#id_text').val(),
                date:$('#id_date').val(),
                category:$('#id_category').val(),
                favorite:$('#id_favorite')[0].checked,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            dataType: "html",
            success: function () {
                alert("Created new note!")
            },
        });
    });

    $(document).on("click","#id_details",function (e) {
        e.preventDefault();
        const id = $(this).context.value;
        console.log(id);
        $.ajax({
            type: "GET",
            url: id,
            data: {
                title:$('#id_title').val(),
                text:$('#id_text').val(),
                date:$('#id_date').val(),
                category:$('#id_category').val(),
                favorite:$('#id_favorite').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            dataType: "html",
            success: clickSuccess,
        });
    });

    $(document).on("click","#id_note_edit",function (e) {
        e.preventDefault();
        const id = $(this).context.value;
        console.log(id);
        $.ajax({
            type: "GET",
            url: "my_notes/edit/"+id,
            data: {
                title:$('#id_title').val(),
                text:$('#id_text').val(),
                date:$('#id_date').val(),
                category:$('#id_category').val(),
                favorite:$('#id_favorite').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            dataType: "html",
            success: clickSuccess,
        });
    });


    $(document).on("change","#filter",function (e) {
        e.preventDefault();

        $.ajax({
            type: 'GET',
            url: '/my_notes/ajax/',
            data: {
                'title': $('#id_title').val(),
                'date': $('#id_date').val(),
                'category': $('#id_category').val(),
                'favorite': $('#id_favorite').val(),
                'order_by': $('#id_order_by').val(),
                'direction': $('#id_direction').val()
            },
            dataType: 'html',
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            success: filterSuccess,
        });
    });


    function clickSuccess(data) {
        $('#ajax').html(data)
    }

    function filterSuccess(data) {
        $('.table').html(data)
    }
});

