import os
import random
from faker import Faker
import file_operations
from file_operations import VERSION
from player_stats import SKILLS, MAPPING_LATTERS, stylize_skills, generate_context


def main():
    os.makedirs("src", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    os.makedirs("output/svg", exist_ok=True)

    fake = Faker("ru_RU")

    for i in range(1, 11):
        random_skills = random.sample(SKILLS, 3)
        stylized_skills = stylize_skills(random_skills, MAPPING_LATTERS)
        context = generate_context(fake, stylized_skills)
        filename = "output/svg/result{}.svg".format(i)
        file_operations.render_template("src/charsheet.svg", filename, context)


if __name__ == '__main__':
    main()