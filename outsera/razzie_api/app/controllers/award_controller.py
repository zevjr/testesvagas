from flask import Blueprint, jsonify

from ..services.award_service import calculate_award_intervals

award_bp = Blueprint('award', __name__, url_prefix='/award')


@award_bp.route('/intervals', methods=['GET'])
def get_award_intervals():
    intervals = calculate_award_intervals()
    if not intervals:
        return jsonify({'min': [], 'max': []})

    min_interval = min(intervals, key=lambda x: x['interval'])
    max_interval = max(intervals, key=lambda x: x['interval'])

    min_intervals = [
        x for x in intervals if x['interval'] == min_interval['interval']
    ]
    max_intervals = [
        x for x in intervals if x['interval'] == max_interval['interval']
    ]

    return jsonify({'min': min_intervals, 'max': max_intervals})
