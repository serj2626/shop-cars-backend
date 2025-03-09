def get_path_for_avatar_car(instance, filename):
    return f"brands/{instance.model_car.brand.title}/{instance.model_car.title}/avatar/{filename}"

def get_path_for_all_images_by_car(instance, filename):
    return f"brands/{instance.car.model_car.brand.title}/{instance.car.model_car.title}/gallery/{filename}"

def get_path_for_avatar_brand(instance, filename):
    return f"brands/{instance.title}/avatar/{filename}"
