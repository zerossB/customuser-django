# Custom User Django

O Django é fornecido com um modelo de usuário interno para autenticação, no entanto, a documentação oficial do Django recomenda o uso de um modelo de usuário personalizado para novos projetos. O motivo é que você deseja fazer alterações no modelo de usuário no futuro – por exemplo, adicionando uma data de nascimento – usando um modelo de usuário personalizado desde o início facilita bastante isso. Mas se não, atualizar o modelo de usuário padrão em um projeto existente do Django é muito, muito desafiador.

Portanto, sempre use um modelo de usuário personalizado para todos os novos projetos do Django. No entanto, o exemplo da documentação oficial não é realmente o que muitos especialistas do Django recomendam usar. Existe uma abordagem muito mais fácil, porém poderosa, para iniciar novos projetos do Django com um modelo de usuário personalizado que eu demonstrarei aqui.

Para saber mais [link do post](https://haynes.blog.br/tecnologia/custom-user-django/) explicando todo o processo