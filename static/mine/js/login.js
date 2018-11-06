$(function () {
    $("#content .login").width(innerWidth)
    var chackAccount = false
    var chackPassword = false
    $('#account input').blur(function () {
        chackAccount = false
        if ($(this).val()=='')
        {
            $('#account i').html('')
            $("#account").removeClass('has-success').removeClass('has-error')
            $("#account span").removeClass("glyphicon-ok").removeClass("glyphicon-remove")
            return
        }
        else
        {
            var re = /^\w{6,12}$/
            if (re.test($(this).val()))
            {
                chackAccount = true
                $('#account i').html('')
                $("#account").removeClass('has-error').addClass("has-success")
                $("#account span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
            }
            else
            {
                $("#account").removeClass('has-success').addClass("has-error")
                $("#account span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
                $('#account i').html('账号错误')
            }
        }
    })
    $('#password input').blur(function () {
        chackPassword = false
         if ($(this).val()=='')
        {
            $('#password i').html('')
            $("#password").removeClass('has-success').removeClass('has-error')
            $("#password span").removeClass("glyphicon-ok").removeClass("glyphicon-remove")
            return
        }
         else
        {
            var re = /^\w{6,12}$/
            if (re.test($(this).val()))
            {
                chackPassword = true
                $('#password i').html('')
                $("#password").removeClass('has-error').addClass("has-success")
                $("#password span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
            }
            else
            {
                $("#password").removeClass('has-success').addClass("has-error")
                $("#password span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
                $('#password i').html('密码错误')
            }
        }
    })

    $('#subButton input').click(function () {

        if (chackAccount && chackPassword)
        {
            console.log('chackAccount' + chackAccount)
            console.log('chackPassword' + chackPassword)
            $('.login form').submit()
        }
        else
        {
             

        }
        // if ($('#account input').val()=='')
        // {
        //     $('#account i').html('账号不能为空!')
        //     $("#account").removeClass('has-success').addClass("has-error")
        //     $("#account span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
        //         // $('#password i').html("")
        //         // $("#password").removeClass('has-error').addClass("has-success")
        //         // $("#password span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
        // }
        // if ($('#password input').val()=='')
        // {
        //     $('#password i').html('账号不能为空!')
        //     $("#password").removeClass('has-success').addClass("has-error")
        //     $("#password span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
        //         // $('#password i').html("")
        //         // $("#password").removeClass('has-error').addClass("has-success")
        //         // $("#password span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
        // }

    })
})