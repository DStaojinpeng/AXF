$(function () {
    $("#content .login").width(innerWidth)
    $('#subButton input').click(function () {

        chackPa = chackPassword()
        chackAcc = chackAccount()
        if (chackAcc && chackPa) {
            $('.login form').submit()
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

    function chackAccount() {
        if ($('#account input').val() == '') {
            $('#account i').html('用户名不能为空')
            $("#account").removeClass('has-success').removeClass('has-error')
            $("#account span").removeClass("glyphicon-ok").removeClass("glyphicon-remove")
            return false
        }
        else {
            var re = /^\w{6,12}$/
            if (re.test($('#account input').val())) {
                $('#account i').html('')
                $("#account").removeClass('has-error').addClass("has-success")
                $("#account span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
                return true
            }
            else {
                $("#account").removeClass('has-success').addClass("has-error")
                $("#account span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
                $('#account i').html('账号错误')
                return false
            }
        }
    }

    function chackPassword() {
        if ($('#password input').val() == '') {
            $('#password i').html('密码不能为空')
            $("#password").removeClass('has-success').removeClass('has-error')
            $("#password span").removeClass("glyphicon-ok").removeClass("glyphicon-remove")
            return false
        }
        else {
            var re = /^\w{6,12}$/
            if (re.test($('#password input').val())) {
                $('#password i').html('')
                $("#password").removeClass('has-error').addClass("has-success")
                $("#password span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
                return true
            }
            else {
                $("#password").removeClass('has-success').addClass("has-error")
                $("#password span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
                $('#password i').html('密码错误')
                return false
            }
        }
    }
})