#!/usr/bin/env python3
import argparse
import sys
import joblib
import numpy as np


def load_model(path="pit_model.pkl"):
    model = joblib.load(path)
    return model


def predict(model, features):
    poly = model["poly"]
    mu = model["mu"]
    sigma = model["sigma"]
    w = model["w"]
    threshold = model["threshold"]

    x = np.array([features], dtype=np.float64)
    x = poly.transform(x)
    x = (x - mu) / sigma
    x = np.hstack([np.ones((x.shape[0], 1)), x])
    prob = 1.0 / (1.0 + np.exp(-x @ w))
    return float(prob.item()), bool(prob >= threshold)


def main():
    parser = argparse.ArgumentParser(
        description="Predict pit stop probability for an F1 lap"
    )
    parser.add_argument(
        "--model", default="pit_model.pkl", help="Path to trained model"
    )
    compound_map = {"SOFT": 0, "MEDIUM": 1, "HARD": 2, "INTERMEDIATE": 3, "WET": 4}
    parser.add_argument(
        "--compound", type=str, required=True,
        choices=list(compound_map),
        help="Tyre compound"
    )
    parser.add_argument("--lap-number", type=float, required=True)
    parser.add_argument("--stint", type=float, required=True)
    parser.add_argument("--tyre-life", type=float, required=True)
    parser.add_argument("--position", type=float, required=True)
    parser.add_argument("--lap-time", type=float, required=True)
    parser.add_argument("--year", type=float, required=True)
    parser.add_argument("--lap-time-delta", type=float, required=True)
    parser.add_argument("--cumulative-degradation", type=float, required=True)
    parser.add_argument("--race-progress", type=float, required=True)
    parser.add_argument("--normalized-tyre-life", type=float, required=True)
    parser.add_argument("--position-change", type=float, required=True)

    args = parser.parse_args()
    model = load_model(args.model)

    features = [
        args.lap_number,
        compound_map[args.compound],
        args.stint,
        args.tyre_life,
        args.position,
        args.lap_time,
        args.year,
        args.lap_time_delta,
        args.cumulative_degradation,
        args.race_progress,
        args.normalized_tyre_life,
        args.position_change,
    ]

    prob, will_pit = predict(model, features)
    print(f"Pit probability: {prob:.4f}")
    print(f"Pit predicted:   {'YES' if will_pit else 'NO'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
