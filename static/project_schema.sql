
CREATE TABLE vendor (
	id INT AUTO_INCREMENT PRIMARY KEY ,
	vendor_name VARCHAR(64),
	vendor_address VARCHAR(512),
	vendor_fax VARCHAR(64),
	create_at DATETIME,
	update_at DATETIME
);

CREATE TABLE business_location (
	id INT AUTO_INCREMENT PRIMARY KEY ,
	business_location_name VARCHAR(64),
	business_location_address VARCHAR(512),
	business_location_type VARCHAR(64),
	create_at DATETIME,
	update_at DATETIME
);

CREATE TABLE machine (
	id INT AUTO_INCREMENT PRIMARY KEY,
	business_location_id INT,
	machine_name VARCHAR(64),
	machine_type VARCHAR(32),
	manufacturer VARCHAR(64),
	create_at DATETIME,
	update_at DATETIME,
	CONSTRAINT fk_machine_business_location FOREIGN KEY (business_location_id) REFERENCES business_location(id)
);


CREATE TABLE contract (
	id INT AUTO_INCREMENT PRIMARY KEY,
	machine_id INT,
	business_location_id INT,
	contract_rate VARCHAR(32),
	start_at DATETIME,
	end_at DATETIME,
	create_at DATETIME,
	update_at DATETIME,
	CONSTRAINT fk_contract_machine FOREIGN KEY (machine_id) REFERENCES machine(id),
	CONSTRAINT fk_contract_business_location FOREIGN KEY (business_location_id) REFERENCES business_location(id)
);


CREATE TABLE product (
	id INT AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR(64),
	manufacturer VARCHAR(64),
	price INT,
	create_at DATETIME,
	update_at DATETIME
);


CREATE TABLE purchase_order (
	id INT AUTO_INCREMENT PRIMARY KEY,
	product_id INT,
	vendor_id INT,
	buyer VARCHAR(64),
	quantity INT,
	create_at DATETIME,
	update_at DATETIME,
	CONSTRAINT fk_purchase_order_product FOREIGN KEY (product_id) REFERENCES product(id),
	CONSTRAINT fk_purchase_order_vendor FOREIGN KEY (vendor_id) REFERENCES vendor(id)
);


CREATE TABLE technician (
	id INT AUTO_INCREMENT PRIMARY KEY,
	technician_name VARCHAR(64),
	create_at DATETIME,
	update_at DATETIME
);


CREATE TABLE orders (
	id INT AUTO_INCREMENT PRIMARY KEY,
	machine_id INT,
	technician_id INT,
	business_location_id INT,
	create_at DATETIME,
	update_at DATETIME,
	CONSTRAINT fk_order_machine FOREIGN KEY (machine_id) REFERENCES machine(id),
	CONSTRAINT fk_order_technician FOREIGN KEY (technician_id) REFERENCES technician(id),
	CONSTRAINT fk_order_business_location FOREIGN KEY (business_location_id) REFERENCES business_location(id)
);


CREATE TABLE purchase_request (
	id INT AUTO_INCREMENT PRIMARY KEY,
	business_location_id INT,
	product_id INT,
	create_at DATETIME,
	update_at DATETIME,
	CONSTRAINT fk_purchase_request_business_location FOREIGN KEY (business_location_id) REFERENCES business_location(id),
	CONSTRAINT fk_purchase_request_product FOREIGN KEY (product_id) REFERENCES product(id)
);


CREATE TABLE invoice (
	id INT AUTO_INCREMENT PRIMARY KEY,
	vendor_id INT,
	product_id INT,
	purchase_order_id INT,
	create_at DATETIME,
	update_at DATETIME,
	CONSTRAINT fk_invoice_vendor FOREIGN KEY (vendor_id) REFERENCES vendor(id),
	CONSTRAINT fk_invoice_product FOREIGN KEY (product_id) REFERENCES product(id),
	CONSTRAINT fk_invoice_purchase_order FOREIGN KEY (purchase_order_id) REFERENCES purchase_order(id)
);







