function Calculate()
{
  document.getElementById('total').placeholder="";
  var price_v = document.getElementById('price').value;
  var amount_v = document.getElementById('amount').value; 
  var total_v = price_v * amount_v;
  document.getElementById('total').value=total_v;
  // document.signupForm.submit();
}

function numbersonly(myfield, e, dec)
{
  var key;
   var keychar;
   if (window.event)
    key = window.event.keyCode;
    else if (e)
     key = e.which;
     else return true;
      keychar = String.fromCharCode(key);
       if ((key==null) || (key==0) || (key==8) || (key==9) || (key==13) || (key==27) ) return true;
        else if ((("0123456789").indexOf(keychar) > -1))
        return true;
         else if (dec && (keychar == "."))
         {
          myfield.form.elements[dec].focus();
           return false;
           }
            else return false;
        }

