from docxtpl import DocxTemplate


class Contract:
    def __init__(self, info_contract: dict, contract_type: str, template: str = 'М'):
        template_path = f"Templates/{template.upper()}{contract_type}.docx"
        # template_path = "Templates/МЗ.docx"
        self.path_to_save_doc = "Contracts/docs/"
        self.template = template
        self.doc = DocxTemplate(template_path)
        self.info = info_contract
        self.context = None

    def render_general(self) -> None:
        general_info = self.info
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
    def render_customer(self) -> None:
        customer_info = self.info
        context = self.context

        context["price_customer"] = customer_info.get("price_customer")
        context["info_customer"] = customer_info.get("info_customer")
        context["full_org_name_customer"] = customer_info.get("full_org_name_customer")
        context["short_org_name_customer"] = customer_info.get("short_org_name_customer")

        self.doc.render(context)

    def save_docx(self) -> str:
        try:
            date_document = self.info.get("date")
            flight_info = self.info.get("flight")
            name_file = f"Заявка_заказчика_{flight_info}_{date_document}_{self.template}.docx"
            path_to_customer = self.path_to_save_doc + f"{name_file}"
            self.doc.save(path_to_customer)
            return name_file
        except Exception as error:
            raise Exception(f"Ошибка создания документа: {error}")


class Driver(Contract):
    def render_driver(self) -> None:
        driver_info = self.info
        context = self.context

        context["price_driver"] = driver_info.get("price_driver")
        context["carrier_info"] = driver_info.get("carrier_info")
        context["full_org_name_carrier"] = driver_info.get("full_org_name_carrier")
        context["short_org_name_carrier"] = driver_info.get("short_org_name_carrier")

        self.doc.render(context)

    def save_docx(self) -> str:
        try:
            date_document = self.info.get("date")
            flight_info = self.info.get("flight")
            name_file = f"Заявка_перевозчика_{flight_info}_{date_document}_{self.template}.docx"
            path_to_driver = self.path_to_save_doc + f"{name_file}"
            self.doc.save(path_to_driver)
            return name_file
        except Exception as error:
            raise Exception(f"Ошибка создания документа: {error}")


def fill_doc(info_doc: dict) -> tuple:
    template = info_doc.get("template")

    customer = Customer(info_contract=info_doc, contract_type='З', template=template)
    customer.render_general()
    customer.render_customer()
    customer_result = customer.save_docx()

    driver = Driver(info_contract=info_doc, contract_type='П', template=template)
    driver.render_general()
    driver.render_driver()
    driver_result = driver.save_docx()

    return customer_result, driver_result


