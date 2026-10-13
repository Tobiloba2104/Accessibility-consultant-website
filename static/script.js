document.addEventListener('DOMContentLoaded', function () {
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(function (link) {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });


  const emailInput = document.getElementById('email');
  if (emailInput) {
    emailInput.addEventListener('blur', function () {
      if (emailInput.value && !emailInput.value.includes('@')) {
        emailInput.setCustomValidity('Please include an @ in the email address.');
      } else {
        emailInput.setCustomValidity('');
      }
    });
  }

  
  const successMsg = document.querySelector('.form-success');
  if (successMsg) {
    setTimeout(function () {
      successMsg.style.transition = 'opacity 1s';
      successMsg.style.opacity = '0';
    }, 4000);
  }
});