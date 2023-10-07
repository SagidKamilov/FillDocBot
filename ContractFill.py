from docxtpl import DocxTemplate


class Contract:
    def __init__(self, info_contract, contract_type, template='Б'):
        if contract_type == "З":
            self.doc = DocxTemplate(f"Templates/{template}З.docx")
        elif contract_type == "П":
            self.doc = DocxTemplate(f"Templates/{template}П.docx")

        self.info = info_contract
        self.context = None

    def render_general(self):
        general_info = self.info.get("general")

        self.context = {
            "date": general_info.get("date"),
            "from_address": general_info.get("from_address"),
            "from_date": general_info.get("from_date"),
            "contact_person_from": general_info.get("contact_person_from"),
            "contact_person_from_phone": general_info.get("contact_person_from_phone"),
            "to_address": general_info.get("to_address"),
            "to_date": general_info.get("to_date"),
            "contact_person_to": general_info.get("contact_person_to"),
            "contact_person_to_phone": general_info.get("contact_person_to_phone"),
            "type_machine": general_info.get("type_machine"),
            "name_cargo": general_info.get("name_cargo"),
            "type_loading": general_info.get("type_loading"),
            "type_unloading": general_info.get("type_unloading"),
            "vat": general_info.get("vat"),
            "car_number": general_info.get("car_number"),
            "car_model": general_info.get("car_model"),
            "trailer_number": general_info.get("trailer_number"),
            "trailer_model": general_info.get("trailer_model"),
            "name_driver": general_info.get("name_driver"),
            "phone_driver": general_info.get("phone_driver"),
            "passport_driver": general_info.get("passport_driver"),
            "contact_manager": general_info.get("contact_manager"),
            "code_ati": general_info.get("code_ati")
        }


class Customer(Contract):
    def render_customer(self):
        customer_info = self.info.get("customer")
        context = self.context

        context["price_customer"] = customer_info.get("price_customer")
        context["info_customer"] = customer_info.get("info_customer")
        context["full_org_name_customer"] = customer_info.get("full_org_name_customer")
        context["short_org_name_customer"] = customer_info.get("short_org_name_customer")

        self.doc.render(context)

    def save_docx(self):
        date_document = self.info.get("date_document")
        flight_info = self.info.get("flight_info")

        self.doc.save(f"Contracts/Заявка заказчика {flight_info} {date_document}.docx")


class Driver(Contract):
    def render_driver(self):
        driver_info = self.info.get("driver")
        context = self.context

        context["price_driver"] = driver_info.get("price_driver")
        context["carrier_info"] = driver_info.get("carrier_info")
        context["full_org_name_carrier"] = driver_info.get("full_org_name_carrier")
        context["short_org_name_carrier"] = driver_info.get("short_org_name_carrier")

        self.doc.render(context=context)

    def save_docx(self):
        date_document = self.info.get("general").get("date")
        flight_info = self.info.get("general").get("from_address") + self.info.get("general").get("to_address")
        self.doc.save(f"Contracts/Заявка перевозчика {flight_info} {date_document}.docx")


info = {
    "general": {
        "date": "02.10.2023",
        "from_address": "3",
        "from_date": "4",
        "contact_person_from": "5",
        "contact_person_from_phone": "6",

        "to_address": "7",
        "to_date": "8",
        "contact_person_to": "9",
        "contact_person_to_phone": "10",

        "type_machine": "11",
        "name_cargo": "12",
        "type_loading": "13",
        "type_unloading": "14",
        "vat": "15",
        "car_number": "16",
        "car_model": "17",
        "trailer_number": "18",
        "trailer_model": "19",
        "name_driver": "20",
        "phone_driver": "21",
        "passport_driver": "22",
        "contact_manager": "23",
        "code_ati": "24"
    },
    "customer": {
        "price_customer": "23",
        "info_customer": "23",
        "full_org_name_customer": "23",
        "short_org_name_customer": "23"
    },
    "driver": {
        "price_driver": "12323",
        "carrier_info": "Паспорт",
        "full_org_name_carrier": "23",
        "short_org_name_carrier": "23"
    }
}

customer = Customer(info_contract=info, contract_type='З')
customer.render_general()
customer.render_customer()
customer.save_docx()

driver = Driver(info_contract=info, contract_type='П')
driver.render_general()
driver.render_driver()
driver.save_docx()
