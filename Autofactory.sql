-- Crear base de datos
CREATE DATABASE IF NOT EXISTS autofactory;
USE autofactory;

-- =====================================================
-- CREACIÓN DE TABLAS
-- =====================================================

-- 1. TABLA MODELOS DE VEHÍCULOS
CREATE TABLE modelos_vehiculos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo_unico VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    categoria ENUM('sedan', 'SUV', 'pickup') NOT NULL,
    versiones TEXT,
    especificaciones_tecnicas TEXT,
    componentes_requeridos TEXT,
    tiempo_estandar_ensamblaje INT COMMENT 'En minutos',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

-- 2. TABLA LÍNEAS DE PRODUCCIÓN
CREATE TABLE lineas_produccion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero_linea VARCHAR(10) UNIQUE NOT NULL,
    tipo_vehiculos_ensambla VARCHAR(100),
    capacidad_diaria INT,
    numero_estaciones_trabajo INT,
    supervisor_responsable VARCHAR(100),
    turno_activo ENUM('mañana', 'tarde', 'noche') NOT NULL,
    estado_operativo ENUM('activo', 'mantenimiento', 'parado') DEFAULT 'activo',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. TABLA COMPONENTES Y PARTES
CREATE TABLE componentes_partes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    codigo_unico VARCHAR(20) UNIQUE NOT NULL,
    descripcion TEXT NOT NULL,
    categoria VARCHAR(50),
    especificaciones_tecnicas TEXT,
    proveedor_principal VARCHAR(100),
    tiempo_entrega_promedio INT COMMENT 'En días',
    costo_unitario DECIMAL(10, 2),
    stock_minimo_requerido INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. TABLA INVENTARIO DE COMPONENTES
CREATE TABLE inventario_componentes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    componente_id INT,
    cantidad_disponible INT DEFAULT 0,
    ubicacion_almacen VARCHAR(50),
    fecha_ultima_entrada DATE,
    calidad ENUM('aprobado', 'en revision', 'rechazado') DEFAULT 'aprobado',
    FOREIGN KEY (componente_id) REFERENCES componentes_partes(id) ON DELETE CASCADE
);

-- 5. TABLA ÓRDENES DE PRODUCCIÓN
CREATE TABLE ordenes_produccion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero_unico VARCHAR(20) UNIQUE NOT NULL,
    fecha_emision DATE NOT NULL,
    modelo_vehiculo_id INT,
    cantidad_producir INT NOT NULL,
    fecha_inicio_programada DATE,
    fecha_finalizacion_estimada DATE,
    prioridad ENUM('baja', 'normal', 'alta', 'urgente') DEFAULT 'normal',
    estado_actual ENUM('pendiente', 'en_proceso', 'completada', 'cancelada') DEFAULT 'pendiente',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (modelo_vehiculo_id) REFERENCES modelos_vehiculos(id)
);

SHOW TABLES;
-- =====================================================
-- PROCEDIMIENTOS ALMACENADOS PARA MÓDULOS
-- =====================================================

-- MÓDULO 1: PROCEDIMIENTOS PARA MODELOS DE VEHÍCULOS

DELIMITER //

-- Obtener todos los modelos activos
CREATE PROCEDURE sp_obtener_modelos()
BEGIN
    SELECT * FROM modelos_vehiculos WHERE activo = TRUE ORDER BY nombre;
END //

-- Obtener modelo por ID
CREATE PROCEDURE sp_obtener_modelo_por_id(IN p_id INT)
BEGIN
    SELECT * FROM modelos_vehiculos WHERE id = p_id;
END //

-- Crear nuevo modelo
CREATE PROCEDURE sp_crear_modelo(
    IN p_codigo_unico VARCHAR(20),
    IN p_nombre VARCHAR(100),
    IN p_categoria ENUM('sedan', 'SUV', 'pickup'),
    IN p_versiones TEXT,
    IN p_especificaciones_tecnicas TEXT,
    IN p_componentes_requeridos TEXT,
    IN p_tiempo_estandar_ensamblaje INT
)
BEGIN
    INSERT INTO modelos_vehiculos (
        codigo_unico, nombre, categoria, versiones, 
        especificaciones_tecnicas, componentes_requeridos, tiempo_estandar_ensamblaje
    ) VALUES (
        p_codigo_unico, p_nombre, p_categoria, p_versiones,
        p_especificaciones_tecnicas, p_componentes_requeridos, p_tiempo_estandar_ensamblaje
    );
    SELECT LAST_INSERT_ID() AS id;
END //

-- Actualizar modelo
CREATE PROCEDURE sp_actualizar_modelo(
    IN p_id INT,
    IN p_codigo_unico VARCHAR(20),
    IN p_nombre VARCHAR(100),
    IN p_categoria ENUM('sedan', 'SUV', 'pickup'),
    IN p_versiones TEXT,
    IN p_especificaciones_tecnicas TEXT,
    IN p_componentes_requeridos TEXT,
    IN p_tiempo_estandar_ensamblaje INT
)
BEGIN
    UPDATE modelos_vehiculos SET
        codigo_unico = p_codigo_unico,
        nombre = p_nombre,
        categoria = p_categoria,
        versiones = p_versiones,
        especificaciones_tecnicas = p_especificaciones_tecnicas,
        componentes_requeridos = p_componentes_requeridos,
        tiempo_estandar_ensamblaje = p_tiempo_estandar_ensamblaje
    WHERE id = p_id;
    SELECT ROW_COUNT() AS filas_afectadas;
END //

-- Eliminar modelo (lógico)
CREATE PROCEDURE sp_eliminar_modelo(IN p_id INT)
BEGIN
    UPDATE modelos_vehiculos SET activo = FALSE WHERE id = p_id;
    SELECT ROW_COUNT() AS filas_afectadas;
END //

-- MÓDULO 2: PROCEDIMIENTOS PARA LÍNEAS DE PRODUCCIÓN

-- Obtener todas las líneas
CREATE PROCEDURE sp_obtener_lineas()
BEGIN
    SELECT * FROM lineas_produccion ORDER BY numero_linea;
END //

-- Obtener línea por ID
CREATE PROCEDURE sp_obtener_linea_por_id(IN p_id INT)
BEGIN
    SELECT * FROM lineas_produccion WHERE id = p_id;
END //

-- Crear nueva línea
CREATE PROCEDURE sp_crear_linea(
    IN p_numero_linea VARCHAR(10),
    IN p_tipo_vehiculos_ensambla VARCHAR(100),
    IN p_capacidad_diaria INT,
    IN p_numero_estaciones_trabajo INT,
    IN p_supervisor_responsable VARCHAR(100),
    IN p_turno_activo ENUM('mañana', 'tarde', 'noche'),
    IN p_estado_operativo ENUM('activo', 'mantenimiento', 'parado')
)
BEGIN
    INSERT INTO lineas_produccion (
        numero_linea, tipo_vehiculos_ensambla, capacidad_diaria,
        numero_estaciones_trabajo, supervisor_responsable, turno_activo, estado_operativo
    ) VALUES (
        p_numero_linea, p_tipo_vehiculos_ensambla, p_capacidad_diaria,
        p_numero_estaciones_trabajo, p_supervisor_responsable, p_turno_activo, p_estado_operativo
    );
    SELECT LAST_INSERT_ID() AS id;
END //

-- Actualizar línea
CREATE PROCEDURE sp_actualizar_linea(
    IN p_id INT,
    IN p_numero_linea VARCHAR(10),
    IN p_tipo_vehiculos_ensambla VARCHAR(100),
    IN p_capacidad_diaria INT,
    IN p_numero_estaciones_trabajo INT,
    IN p_supervisor_responsable VARCHAR(100),
    IN p_turno_activo ENUM('mañana', 'tarde', 'noche'),
    IN p_estado_operativo ENUM('activo', 'mantenimiento', 'parado')
)
BEGIN
    UPDATE lineas_produccion SET
        numero_linea = p_numero_linea,
        tipo_vehiculos_ensambla = p_tipo_vehiculos_ensambla,
        capacidad_diaria = p_capacidad_diaria,
        numero_estaciones_trabajo = p_numero_estaciones_trabajo,
        supervisor_responsable = p_supervisor_responsable,
        turno_activo = p_turno_activo,
        estado_operativo = p_estado_operativo
    WHERE id = p_id;
    SELECT ROW_COUNT() AS filas_afectadas;
END //

-- Cambiar estado de línea
CREATE PROCEDURE sp_cambiar_estado_linea(
    IN p_id INT,
    IN p_estado_operativo ENUM('activo', 'mantenimiento', 'parado')
)
BEGIN
    UPDATE lineas_produccion SET estado_operativo = p_estado_operativo WHERE id = p_id;
    SELECT ROW_COUNT() AS filas_afectadas;
END //

-- MÓDULO 3: PROCEDIMIENTOS PARA COMPONENTES Y PARTES

-- Obtener todos los componentes
CREATE PROCEDURE sp_obtener_componentes()
BEGIN
    SELECT * FROM componentes_partes ORDER BY descripcion;
END //

-- Obtener componente por ID
CREATE PROCEDURE sp_obtener_componente_por_id(IN p_id INT)
BEGIN
    SELECT * FROM componentes_partes WHERE id = p_id;
END //

-- Crear nuevo componente
CREATE PROCEDURE sp_crear_componente(
    IN p_codigo_unico VARCHAR(20),
    IN p_descripcion TEXT,
    IN p_categoria VARCHAR(50),
    IN p_especificaciones_tecnicas TEXT,
    IN p_proveedor_principal VARCHAR(100),
    IN p_tiempo_entrega_promedio INT,
    IN p_costo_unitario DECIMAL(10, 2),
    IN p_stock_minimo_requerido INT
)
BEGIN
    INSERT INTO componentes_partes (
        codigo_unico, descripcion, categoria, especificaciones_tecnicas,
        proveedor_principal, tiempo_entrega_promedio, costo_unitario, stock_minimo_requerido
    ) VALUES (
        p_codigo_unico, p_descripcion, p_categoria, p_especificaciones_tecnicas,
        p_proveedor_principal, p_tiempo_entrega_promedio, p_costo_unitario, p_stock_minimo_requerido
    );
    SELECT LAST_INSERT_ID() AS id;
END //

-- Actualizar componente
CREATE PROCEDURE sp_actualizar_componente(
    IN p_id INT,
    IN p_codigo_unico VARCHAR(20),
    IN p_descripcion TEXT,
    IN p_categoria VARCHAR(50),
    IN p_especificaciones_tecnicas TEXT,
    IN p_proveedor_principal VARCHAR(100),
    IN p_tiempo_entrega_promedio INT,
    IN p_costo_unitario DECIMAL(10, 2),
    IN p_stock_minimo_requerido INT
)
BEGIN
    UPDATE componentes_partes SET
        codigo_unico = p_codigo_unico,
        descripcion = p_descripcion,
        categoria = p_categoria,
        especificaciones_tecnicas = p_especificaciones_tecnicas,
        proveedor_principal = p_proveedor_principal,
        tiempo_entrega_promedio = p_tiempo_entrega_promedio,
        costo_unitario = p_costo_unitario,
        stock_minimo_requerido = p_stock_minimo_requerido
    WHERE id = p_id;
    SELECT ROW_COUNT() AS filas_afectadas;
END //

-- Obtener inventario completo
CREATE PROCEDURE sp_obtener_inventario_completo()
BEGIN
    SELECT 
        cp.*,
        ic.cantidad_disponible,
        ic.ubicacion_almacen,
        ic.fecha_ultima_entrada,
        ic.calidad,
        CASE 
            WHEN ic.cantidad_disponible <= cp.stock_minimo_requerido THEN 'CRÍTICO'
            WHEN ic.cantidad_disponible <= cp.stock_minimo_requerido * 1.5 THEN 'BAJO'
            ELSE 'NORMAL'
        END AS nivel_stock
    FROM componentes_partes cp
    LEFT JOIN inventario_componentes ic ON cp.id = ic.componente_id;
END //

-- MÓDULO 4: PROCEDIMIENTOS PARA ÓRDENES DE PRODUCCIÓN

-- Obtener todas las órdenes
CREATE PROCEDURE sp_obtener_ordenes()
BEGIN
    SELECT 
        op.*,
        mv.nombre AS modelo_nombre,
        mv.codigo_unico AS modelo_codigo
    FROM ordenes_produccion op
    JOIN modelos_vehiculos mv ON op.modelo_vehiculo_id = mv.id
    ORDER BY op.fecha_emision DESC;
END //

-- Obtener orden por ID
CREATE PROCEDURE sp_obtener_orden_por_id(IN p_id INT)
BEGIN
    SELECT 
        op.*,
        mv.nombre AS modelo_nombre,
        mv.codigo_unico AS modelo_codigo
    FROM ordenes_produccion op
    JOIN modelos_vehiculos mv ON op.modelo_vehiculo_id = mv.id
    WHERE op.id = p_id;
END //

-- Crear nueva orden
CREATE PROCEDURE sp_crear_orden(
    IN p_numero_unico VARCHAR(20),
    IN p_fecha_emision DATE,
    IN p_modelo_vehiculo_id INT,
    IN p_cantidad_producir INT,
    IN p_fecha_inicio_programada DATE,
    IN p_fecha_finalizacion_estimada DATE,
    IN p_prioridad ENUM('baja', 'normal', 'alta', 'urgente')
)
BEGIN
    INSERT INTO ordenes_produccion (
        numero_unico, fecha_emision, modelo_vehiculo_id, cantidad_producir,
        fecha_inicio_programada, fecha_finalizacion_estimada, prioridad
    ) VALUES (
        p_numero_unico, p_fecha_emision, p_modelo_vehiculo_id, p_cantidad_producir,
        p_fecha_inicio_programada, p_fecha_finalizacion_estimada, p_prioridad
    );
    SELECT LAST_INSERT_ID() AS id;
END //

-- Actualizar estado de orden
CREATE PROCEDURE sp_actualizar_estado_orden(
    IN p_id INT,
    IN p_estado_actual ENUM('pendiente', 'en_proceso', 'completada', 'cancelada')
)
BEGIN
    UPDATE ordenes_produccion SET estado_actual = p_estado_actual WHERE id = p_id;
    SELECT ROW_COUNT() AS filas_afectadas;
END //

-- Obtener órdenes por estado
CREATE PROCEDURE sp_obtener_ordenes_por_estado(
    IN p_estado ENUM('pendiente', 'en_proceso', 'completada', 'cancelada')
)
BEGIN
    SELECT 
        op.*,
        mv.nombre AS modelo_nombre
    FROM ordenes_produccion op
    JOIN modelos_vehiculos mv ON op.modelo_vehiculo_id = mv.id
    WHERE op.estado_actual = p_estado
    ORDER BY op.prioridad DESC, op.fecha_inicio_programada;
END //

DELIMITER ;

-- =====================================================
-- INSERCIÓN DE DATOS DE PRUEBA (10 por tabla)
-- =====================================================

-- DATOS PARA MODELOS DE VEHÍCULOS
INSERT INTO modelos_vehiculos (codigo_unico, nombre, categoria, versiones, especificaciones_tecnicas, componentes_requeridos, tiempo_estandar_ensamblaje) VALUES
('MOD-SED-001', 'EcoSedán 2024', 'sedan', 'Base, Comfort, Luxury', 'Motor 1.6L, 120HP, Transmisión manual/automática', 'Chasis, Motor, Transmisión, Ruedas, Asientos, Electrónica', 480),
('MOD-SED-002', 'FamilySedán Plus', 'sedan', 'Familiar, Executive', 'Motor 2.0L, 150HP, Transmisión automática CVT', 'Chasis reforzado, Motor 2.0L, Transmisión CVT, Ruedas 17", Asientos cuero', 540),
('MOD-SUV-001', 'Trail Explorer', 'SUV', '4x2, 4x4, Premium', 'Motor 2.5L, 180HP, Tracción integral', 'Chasis SUV, Motor 2.5L, Transmisión 4x4, Ruedas 18", Sistema off-road', 600),
('MOD-SUV-002', 'Urban Adventure', 'SUV', 'City, Cross', 'Motor 1.8L, 140HP, Altura elevada', 'Chasis crossover, Motor 1.8L, Transmisión automática, Ruedas 17"', 520),
('MOD-PIC-001', 'WorkMaster Pro', 'pickup', 'Cabina simple, Cabina doble', 'Motor 3.0L Turbo Diesel, 200HP, Carga útil 1000kg', 'Chasis reforzado, Motor Diesel, Suspensión pesada, Caja de carga', 660),
('MOD-PIC-002', 'Ranger Duty', 'pickup', 'Base, Work, Premium', 'Motor 2.8L Diesel, 180HP, Tracción 4x4', 'Chasis doble viga, Motor 2.8L, Transmisión manual 6vel, Ruedas 17"', 620),
('MOD-SED-003', 'City Compact', 'sedan', 'Eco, Sport', 'Motor 1.4L, 100HP, Económico', 'Chasis compacto, Motor 1.4L, Transmisión manual, Ruedas 15"', 420),
('MOD-SUV-003', 'Mountain King', 'SUV', 'Off-road, Expedition', 'Motor 3.0L V6, 250HP, Tracción 4x4 reductora', 'Chasis robusto, Motor V6, Diferenciales bloqueables, Ruedas 20"', 720),
('MOD-PIC-003', 'Cargo Express', 'pickup', 'Estándar, Larga distancia', 'Motor 2.5L Diesel, 160HP, Capacidad 1200kg', 'Chasis largo, Motor 2.5L, Suspensión reforzada, Frenos ABS', 580),
('MOD-SED-004', 'Luxury Executive', 'sedan', 'Premium, Black Edition', 'Motor 2.5L V6, 220HP, Asientos de cuero, Techo panorámico', 'Chasis premium, Motor V6, Asientos eléctricos, Sistema multimedia', 640);

-- DATOS PARA LÍNEAS DE PRODUCCIÓN
INSERT INTO lineas_produccion (numero_linea, tipo_vehiculos_ensambla, capacidad_diaria, numero_estaciones_trabajo, supervisor_responsable, turno_activo, estado_operativo) VALUES
('L01', 'Sedanes compactos', 50, 12, 'Carlos Rodríguez', 'mañana', 'activo'),
('L02', 'Sedanes familiares', 45, 14, 'María González', 'mañana', 'activo'),
('L03', 'SUVs urbanos', 35, 16, 'Juan Pérez', 'tarde', 'activo'),
('L04', 'SUVs off-road', 25, 18, 'Ana Martínez', 'tarde', 'activo'),
('L05', 'Pickups livianas', 30, 15, 'Pedro Sánchez', 'mañana', 'activo'),
('L06', 'Pickups pesadas', 20, 20, 'Luisa Fernández', 'noche', 'mantenimiento'),
('L07', 'Sedanes premium', 15, 22, 'Roberto Gómez', 'mañana', 'activo'),
('L08', 'SUVs híbridas', 20, 18, 'Patricia Díaz', 'tarde', 'activo'),
('L09', 'Pickups doble cabina', 25, 16, 'Fernando López', 'noche', 'activo'),
('L10', 'Modelos especiales', 10, 25, 'Gabriela Ruiz', 'mañana', 'parado');

-- DATOS PARA COMPONENTES Y PARTES
INSERT INTO componentes_partes (codigo_unico, descripcion, categoria, especificaciones_tecnicas, proveedor_principal, tiempo_entrega_promedio, costo_unitario, stock_minimo_requerido) VALUES
('COMP-MOT-001', 'Motor 1.6L 16v', 'Motor', '4 cilindros, 1600cc, 120HP, Inyección electrónica', 'Motores del Sur S.A.', 15, 2500.00, 50),
('COMP-MOT-002', 'Motor 2.0L 16v', 'Motor', '4 cilindros, 2000cc, 150HP, Turbo', 'Motores del Sur S.A.', 20, 3800.00, 30),
('COMP-TRA-001', 'Transmisión manual 5vel', 'Transmisión', 'Manual 5 velocidades, Tracción delantera', 'Transmisiones Andinas', 10, 1200.00, 40),
('COMP-TRA-002', 'Transmisión automática CVT', 'Transmisión', 'CVT, Modo secuencial, Tracción delantera', 'Transmisiones Andinas', 18, 2100.00, 25),
('COMP-RUE-001', 'Ruedas 15" acero', 'Ruedas', 'Llantas de acero 15", Neumáticos 195/65R15', 'Neumáticos del Pacífico', 5, 350.00, 200),
('COMP-RUE-002', 'Ruedas 17" aleación', 'Ruedas', 'Llantas de aleación 17", Neumáticos 215/55R17', 'Neumáticos del Pacífico', 7, 580.00, 150),
('COMP-ASI-001', 'Asientos tela', 'Interior', 'Asientos delanteros y traseros, Tela respirable', 'Interiores Automotrices', 12, 450.00, 100),
('COMP-ASI-002', 'Asientos cuero', 'Interior', 'Asientos premium, Cuero ecológico, Calefacción', 'Interiores Automotrices', 20, 950.00, 60),
('COMP-ELE-001', 'Sistema multimedia', 'Electrónica', 'Pantalla 7", GPS, Bluetooth, Cámara trasera', 'Electrónica Automotriz', 14, 650.00, 80),
('COMP-FRE-001', 'Sistema frenos ABS', 'Frenos', 'Discos ventilados delanteros, Tambores traseros, ABS', 'Frenos Seguros S.A.', 8, 430.00, 120);

-- DATOS PARA INVENTARIO DE COMPONENTES
INSERT INTO inventario_componentes (componente_id, cantidad_disponible, ubicacion_almacen, fecha_ultima_entrada, calidad) VALUES
(1, 45, 'A1-B2-C3', '2024-10-15', 'aprobado'),
(2, 28, 'A1-B3-C1', '2024-10-18', 'aprobado'),
(3, 35, 'B2-C1-D2', '2024-10-20', 'aprobado'),
(4, 22, 'B2-C2-D1', '2024-10-17', 'en revision'),
(5, 180, 'C1-D1-E1', '2024-10-22', 'aprobado'),
(6, 120, 'C1-D2-E2', '2024-10-21', 'aprobado'),
(7, 85, 'D1-E1-F1', '2024-10-19', 'aprobado'),
(8, 45, 'D2-E2-F2', '2024-10-16', 'aprobado'),
(9, 65, 'E1-F1-G1', '2024-10-14', 'rechazado'),
(10, 100, 'E2-F2-G2', '2024-10-23', 'aprobado');

-- DATOS PARA ÓRDENES DE PRODUCCIÓN
INSERT INTO ordenes_produccion (numero_unico, fecha_emision, modelo_vehiculo_id, cantidad_producir, fecha_inicio_programada, fecha_finalizacion_estimada, prioridad, estado_actual) VALUES
('ORD-2024-001', '2024-10-01', 1, 50, '2024-10-15', '2024-10-30', 'alta', 'completada'),
('ORD-2024-002', '2024-10-05', 2, 30, '2024-10-20', '2024-11-05', 'normal', 'en_proceso'),
('ORD-2024-003', '2024-10-08', 3, 25, '2024-10-22', '2024-11-08', 'urgente', 'en_proceso'),
('ORD-2024-004', '2024-10-10', 4, 40, '2024-10-25', '2024-11-12', 'normal', 'pendiente'),
('ORD-2024-005', '2024-10-12', 5, 20, '2024-10-18', '2024-11-02', 'alta', 'completada'),
('ORD-2024-006', '2024-10-15', 6, 15, '2024-10-28', '2024-11-15', 'baja', 'pendiente'),
('ORD-2024-007', '2024-10-18', 7, 35, '2024-11-01', '2024-11-18', 'normal', 'pendiente'),
('ORD-2024-008', '2024-10-20', 8, 10, '2024-10-30', '2024-11-10', 'alta', 'en_proceso'),
('ORD-2024-009', '2024-10-22', 9, 45, '2024-11-05', '2024-11-25', 'normal', 'pendiente'),
('ORD-2024-010', '2024-10-25', 10, 12, '2024-11-08', '2024-11-20', 'urgente', 'pendiente');

CALL sp_obtener_modelos();
CALL sp_obtener_lineas();
CALL sp_obtener_inventario_completo();
CALL sp_obtener_ordenes_por_estado('pendiente');