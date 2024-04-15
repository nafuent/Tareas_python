DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS public.usuario
(
    idusuario serial,
    idrol integer,
    nombre character varying(100) COLLATE pg_catalog."default",
    tipo_documento character varying(20) COLLATE pg_catalog."default",
    num_documento character varying(20) COLLATE pg_catalog."default",
    direccion character varying(70) COLLATE pg_catalog."default",
    telefono character varying(20) COLLATE pg_catalog."default",
    email character varying(50) COLLATE pg_catalog."default",
    clave character varying(1000) COLLATE pg_catalog."default",
    estado integer,
    CONSTRAINT usuario_pkey PRIMARY KEY (idusuario)
);

CREATE TABLE IF NOT EXISTS public.rol
(
    idrol  serial,
    nombre character varying(30) COLLATE pg_catalog."default",
    descripcion character varying(255) COLLATE pg_catalog."default",
    estado bit(1),
    CONSTRAINT rol_pkey PRIMARY KEY (idrol)
);

CREATE TABLE IF NOT EXISTS public.articulo
(
    idarticulo serial,
    idcategoria integer,
    codigo character varying(50) COLLATE pg_catalog."default",
    nombre character varying(100) COLLATE pg_catalog."default",
    precio_venta numeric(11, 2),
    stock integer,
    descripcion character varying(255) COLLATE pg_catalog."default",
    imagen character varying(20) COLLATE pg_catalog."default",
    estado bit(1),
    CONSTRAINT articulo_pkey PRIMARY KEY (idarticulo)
);

CREATE TABLE IF NOT EXISTS public.categoria
(
    idcategoria serial,
    nombre character varying(50) COLLATE pg_catalog."default",
    descripcion character varying(255) COLLATE pg_catalog."default",
    estado bit(1),
    CONSTRAINT categoria_pkey PRIMARY KEY (idcategoria)
);

CREATE TABLE IF NOT EXISTS public.venta
(
    idventa serial,
    idcliente integer,
    idusuario integer,
    tipo_comprobante character varying(20) COLLATE pg_catalog."default",
    serie_comprobante character varying(7) COLLATE pg_catalog."default",
    num_comprobante character varying(10) COLLATE pg_catalog."default",
    fecha date,
    impuesto numeric(4, 2),
    total numeric(11, 2),
    estado character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT venta_pkey PRIMARY KEY (idventa)
);

CREATE TABLE IF NOT EXISTS public.persona
(
    idpersona serial,
    tipo_persona character varying(20) COLLATE pg_catalog."default",
    nombre character varying(100) COLLATE pg_catalog."default",
    tipo_documento character varying(20) COLLATE pg_catalog."default",
    num_documento character varying(20) COLLATE pg_catalog."default",
    direccion character varying(70) COLLATE pg_catalog."default",
    telefono character varying(20) COLLATE pg_catalog."default",
    email character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT persona_pkey PRIMARY KEY (idpersona)
);

CREATE TABLE IF NOT EXISTS public.detalle_venta
(
    iddetalle_venta serial,
    idventa integer,
    idarticulo integer,
    cantidad integer,
    precio numeric(11, 2),
    descuento numeric(11, 2),
    CONSTRAINT detalle_venta_pkey PRIMARY KEY (iddetalle_venta)
);

CREATE TABLE IF NOT EXISTS public.ingreso
(
    idingreso serial,
    idproveedor integer,
    idusuario integer,
    tipo_comprobante character varying(20) COLLATE pg_catalog."default",
    serie_comprobante character varying(7) COLLATE pg_catalog."default",
    num_comprobante character varying(10) COLLATE pg_catalog."default",
    fecha date,
    impuesto numeric(4, 2),
    total numeric(11, 2),
    estado character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT ingreso_pkey PRIMARY KEY (idingreso)
);

CREATE TABLE IF NOT EXISTS public.detalle_ingreso
(
    iddetalle_ingreso serial,
    idingreso integer,
    idarticulo integer,
    cantidad integer,
    precio numeric(11, 2),
    CONSTRAINT detalle_ingreso_pkey PRIMARY KEY (iddetalle_ingreso)
);

ALTER TABLE IF EXISTS public.usuario
    ADD FOREIGN KEY (idrol)
    REFERENCES public.rol (idrol) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.articulo
    ADD FOREIGN KEY (idcategoria)
    REFERENCES public.categoria (idcategoria) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.venta
    ADD FOREIGN KEY (idcliente)
    REFERENCES public.persona (idpersona) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.venta
    ADD FOREIGN KEY (idusuario)
    REFERENCES public.usuario (idusuario) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.detalle_venta
    ADD FOREIGN KEY (idventa)
    REFERENCES public.venta (idventa) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.detalle_venta
    ADD FOREIGN KEY (idarticulo)
    REFERENCES public.articulo (idarticulo) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.ingreso
    ADD FOREIGN KEY (idproveedor)
    REFERENCES public.persona (idpersona) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.detalle_ingreso
    ADD FOREIGN KEY (idingreso)
    REFERENCES public.ingreso (idingreso) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.detalle_ingreso
    ADD FOREIGN KEY (idarticulo)
    REFERENCES public.articulo (idarticulo) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;
'''