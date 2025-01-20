from sportradar.scoreboard import ScoreBoard

def test_create_empty_scoreboard():
    """Test if empty score board has no matches"""
    board = ScoreBoard()
    assert board.summary == []

def test_add_new_match_to_scoreboard():
    """Test if new match is added"""
    board = ScoreBoard()

    board.add("Mexico", "Brazil")

    assert len(board.summary) == 1