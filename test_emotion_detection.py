"""Integration tests for the five required emotion examples."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Verify dominant emotions against the live Watson service."""

    def test_required_examples(self):
        """Check all five examples specified in the project."""
        examples = (
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        )
        for text, expected in examples:
            with self.subTest(text=text):
                result = emotion_detector(text)
                print(f"{text} -> {result['dominant_emotion']}", flush=True)
                self.assertEqual(result["dominant_emotion"], expected)

    def test_blank_input(self):
        """Ensure blank input returns None for every output field."""
        self.assertTrue(all(value is None
                            for value in emotion_detector("").values()))


if __name__ == "__main__":
    unittest.main()
