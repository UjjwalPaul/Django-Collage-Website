// registration validation

function validation()
{
    var mynm = document.f1.nm.value;
    var myfnm = document.f1.fnm.value;
    var mymail = document.f1.email.value;
    var mymobnum = document.f1.mobnum.value;
    var mybrc = document.f1.brc.value;
    var mydob = document.f1.dob.value;
    var mydob1 = parseInt(mydob);
    var mypass1 = document.f1.pass1.value;
    var mypass2 = document.f1.pass2.value;
    var mygender = document.f1.gender.value;

    if (mynm == "")
    {
        alert("Please enter your name !!!");
        document.f1.nm.focus();
        return false;
    }

    if (myfnm == "")
    {
        alert("Please enter your father name !!!");
        document.f1.fnm.focus();
        return false;
    }

    if (mymail == "")
    {
        alert("Please enter your email !!!");
        document.f1.email.focus();
        return false;
    }

    if (mymobnum == "")
    {
        alert("Please eneter your mobile number !!!")
        document.f1.mobnum.focus();
        return false;
    }

    if (mybrc == "")
    {
        alert("Please enter your branch !!!")
        document.f1.brc.focus();
        return false;
    }

    if (mydob == "")
    {
        alert("Please enter your DOB !!!")
        document.f1.dob.focus();
        return false;
    }

    if (isNaN(mydob1))
	{
	    alert("Please enter numaric age !!!");
		document.f1.dob.value="";
		document.f1.dob.focus();
		return false;
	}

    if (mypass1 == "")
    {
        alert("Please enter your password !!!");
        document.f1.pass1.focus();
        return false;
    }

    if (mypass2 == "")
    {
        alert("Please enter your confim password !!!");
        document.f1.pass2.focus();
        return false;
    }

    if (mypass1 != mypass2)
    {
        alert("Password does not match !!!");
        document.f1.pass1.value="";
        document.f1.pass2.value="";
        document.f1.pass1.focus();
        return false;
    }

    if (mygender == "")
    {
        alert("Please enter your Gender !!!");
        return false;
    }
}

// CAPTCHA

var captcha;
function generate()
 {

    // Clear old input
    document.getElementById("submit").value = "";

    // Access the element to store
    // the generated captcha
    captcha = document.getElementById("image");
    var uniquechar = "";
    
    const randomchar =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    // Generate captcha for length of
    // 5 with random character
    for (let i = 1; i < 5; i++) {
        uniquechar += randomchar.charAt(
            Math.random() * randomchar.length)
        }

    // Store generated input
    captcha.innerHTML = uniquechar;
}

function printmsg() 
{
    const usr_input = document
        .getElementById("submit").value;
        
    // Check whether the input is equal
    // to generated captcha or not
    if (usr_input == captcha.innerHTML) {
        var s = document.getElementById("key")
        alert("Captcha Matched !!!")
        // .innerHTML = "Matched";
        generate();
    }
    else {
        var s = document.getElementById("key")
        alert(" Captcha Does Not-Match !!!")
        // .innerHTML = "not Matched";
        generate();
    }
}


