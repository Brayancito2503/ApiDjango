select * from clientes

select * from rol;
select * from menu	;
select * from menurol;
INSERT INTO Rol (nombrerol) values ('Administrador'),
                                    ('Mesero'),
                                    ('Cajero')

INSERT INTO Menu (nombremenu,icono, url) values ('DashBoard', 'dashboard','/pages/dashboard'),
											('Usuarios','group','/pages/usuarios'),
											('Productos', 'collections_bookmark','/pages/productos'),
											('Venta', 'currency_exchange', '/pages/venta'),
											('Historial Ventas', 'edit_note', '/pages/historial_venta'),
											('Reportes','receipt', '/pages/reportes'),
											('MateriaPrima','collections_bookmark','/pages/materiaprima')
											
INSERT INTO MenuRol (IdMenu, IdRol) values (1,1),
										   (2,1),
										   (3,1),
										   (4,1),
										   (5,1),
										   (6,1),
										   (7,1),
										   (2,2),
										   (4,3),
										   (5,3),
										   (6,3)											