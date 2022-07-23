(() => {
  // Base Authentication JavaScript File
  
  // First add a listener to toggle show password
  // input:checkbox -> id='show_password'
  
  function toggleShowPassword(event) {
    try {
      const pass1 = document.getElementById("id_password") || document.getElementById("id_password1");
      const pass2 = document.getElementById("id_password2");
      if (event.target.checked) {
        if (pass1) pass1.setAttribute("type", "text");
        if (pass2) pass2.setAttribute("type", "text");
      } else {
        if (pass1) pass1.setAttribute("type", "password");
        if (pass2) pass2.setAttribute("type", "password");
      }
    } catch (error) {
      console.log("There is some problem. Please refresh the page.")
    }
  }
  const showPassEl = document.getElementById("show_password");
  showPassEl.addEventListener("change", toggleShowPassword);
})();