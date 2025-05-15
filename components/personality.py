from models.Personality import PersonalityPicker, Personality

personalities = [
    Personality(
        name="The Worker Bee",
        description="You like to start what you finish and keeping things running day-to-day.",
        image_path="./assets/workerbee.png",
        scores = {
            "Extroversion": 8,
            "Conscientiousness": 1,
            "Agreeableness": 8,
            "Honesty-Humility": 1,
            "Emotionality": 1,
            "Openness to Experience": 8
        }
    )
]