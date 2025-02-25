create database if not exists db_comentarios_pantheon;
use db_comentarios_pantheon;

create table if not exists tb_comentarios_pantheon(
	id_comentario int primary key auto_increment,
	data_e_hora datetime,
    nome varchar(30) not null,
    comentario text not null);