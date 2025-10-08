document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const errorMessage = document.getElementById('error-message');

    // Check if Firebase is initialized
    if (typeof firebase === 'undefined' || typeof firebase.auth === 'undefined') {
        errorMessage.textContent = 'Erro na configuração do Firebase. Verifique o console.';
        console.error('Firebase is not properly initialized. Check firebase-config.js');
        return;
    }

    const auth = firebase.auth();

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const email = emailInput.value;
        const password = passwordInput.value;

        errorMessage.textContent = ''; // Clear previous errors

        auth.signInWithEmailAndPassword(email, password)
            .then((userCredential) => {
                // Signed in
                console.log('Login bem-sucedido!', userCredential.user);
                window.location.href = 'portal-franqueado.html';
            })
            .catch((error) => {
                let message = 'Ocorreu um erro ao fazer login.';
                switch (error.code) {
                    case 'auth/user-not-found':
                        message = 'Usuário não encontrado. Verifique o e-mail.';
                        break;
                    case 'auth/wrong-password':
                        message = 'Senha incorreta. Tente novamente.';
                        break;
                    case 'auth/invalid-email':
                        message = 'O formato do e-mail é inválido.';
                        break;
                    default:
                        message = 'Erro: ' + error.message;
                        break;
                }
                errorMessage.textContent = message;
                console.error('Erro de autenticação:', error);
            });
    });
});
