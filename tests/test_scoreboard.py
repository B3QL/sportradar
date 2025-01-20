from sportradar.scoreboard import ScoreBoard

def test_create_empty_scoreboard():
    """Test if empty score board has no matches"""
    board = ScoreBoard()
    assert board.summary == []