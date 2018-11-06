$(function () {
    $(".register").width(innerWidth)
    // 验证账号
    $('#account input').blur(function () {
        if ($(this).val() == '') {
            return
        }
        else {
            var re = /^\w{6,12}$/
            if (re.test($(this).val())) {
                $.get('/chackAccount/', {'account': $(this).val()}, function (reponse) {
                    console.log(reponse)
                    if (reponse.status == 1) {
                        $('#account i').html('')
                        $("#account").removeClass('has-error').addClass("has-success")
                        $("#account span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
                    }
                    else {
                        $("#account").removeClass('has-success').addClass("has-error")
                        $("#account span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
                        $('#account i').html(reponse.content)

                    }
                })
                // $("#account").removeClass('has-error').addClass("has-success")
                // $("#account span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
            }
            else {
                $("#account").removeClass('has-success').addClass("has-error")
                $("#account span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
            }
        }
    })
    // 验证密码
    $('#password input').blur(function () {
        if ($(this).val() == '') {
            return
        }
        else {
            var re = /^\w{6,12}$/
            if (re.test($(this).val())) {
                $('#password i').html("")
                $("#password").removeClass('has-error').addClass("has-success")
                $("#password span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
            }
            else {
                $('#password i').html("密码输入格式错误！")
                $("#password").removeClass('has-success').addClass("has-error")
                $("#password span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
            }
        }
    })
    // 验证密码相等
    $('#repassword input').blur(function () {
        if ($(this).val() == '') {
            return
        }
        else {
            if ($(this).val() == $('#password input').val()) {
                $('#repassword i').html("")
                $("#repassword").removeClass('has-error').addClass("has-success")
                $("#repassword span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
            }
            else {
                $('#repassword i').html("两次输入密码不一致")
                $("#repassword").removeClass('has-success').addClass("has-error")
                $("#repassword span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
            }
        }
    })
    // 验证手机
    $('#tel input').blur(function () {
        if ($(this).val() == '') {
            return
        }
        else {
            var re = /^1(3|4|5|7|8)\d{9}$/
            if (re.test($(this).val())) {
                $.get("/chacktel/", {'tel': $(this).val()}, function (response) {
                    console.log(response)
                    if (response.status==1) {
                        $('#tel i').html('')
                        $("#tel").removeClass('has-error').addClass("has-success")
                        $("#tel span").removeClass("glyphicon-remove").addClass('glyphicon-ok')
                    }
                    else {
                        $('#tel i').html(response.content)
                        $("#tel").removeClass('has-success').addClass("has-error")
                        $("#tel span").removeClass("glyphicon-ok").addClass('glyphicon-remove')

                    }
                })
            }
            else {
                $('#tel i').html("手机号输入错误！")
                $("#tel").removeClass('has-success').addClass("has-error")
                $("#tel span").removeClass("glyphicon-ok").addClass('glyphicon-remove')
            }
        }
    })
})