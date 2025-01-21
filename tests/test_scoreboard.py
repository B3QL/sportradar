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

def test_score_is_zero_zero_for_new_matches():
    """Test if the match initial score is 0-0"""
    board = ScoreBoard()

    board.add("Mexico", "Brazil")

    first_match, = board.summary
    assert first_match.score == (0, 0)

def test_update_score():
    """Test if score of the match is updated"""
    board = ScoreBoard()

    match_id = board.add("Mexico", "Brazil")
    board.update_score(match_id, 1, 0)

    first_match, = board.summary
    assert first_match.score == (1, 0)

def test_remove_match():
    """Test if removed match is not in summary"""
    board = ScoreBoard()
    match_id =  board.add("Mexico", "Brazil")

    board.remove(match_id)

    assert board.summary == []

def test_summary_order_by_total_score():
    """Test if summary return matches with total score descending order"""
    board = ScoreBoard()
    mexcan_match = board.add("Mexico", "Canada")
    board.update_score(mexcan_match, 0, 5)
    spabra_match = board.add("Spain", "Brazil")
    board.update_score(spabra_match, 10, 2)

    first_match, second_match = board.summary

    assert first_match.mid == spabra_match
    assert second_match.mid == mexcan_match

def test_summary_order_by_total_score_more_matches():
    """Test if summary return matches with total score descending order"""
    board = ScoreBoard()
    poleng_match = board.add("Poland", "England")
    mexcan_match = board.add("Mexico", "Canada")
    board.update_score(mexcan_match, 0, 5)
    spabra_match = board.add("Spain", "Brazil")
    board.update_score(spabra_match, 10, 2)


    first_match, second_match, third_match = board.summary

    assert first_match.mid == spabra_match
    assert second_match.mid == mexcan_match
    assert third_match.mid == poleng_match

def test_summary_order_with_same_score():
    """Test if matches with the same score are ordered by the start time"""
    board = ScoreBoard()
    poleng_match = board.add("Poland", "England")
    mexcan_match = board.add("Mexico", "Canada")
    spabra_match = board.add("Spain", "Brazil")

    first_match, second_match, third_match = board.summary

    assert first_match.mid == spabra_match
    assert second_match.mid == mexcan_match
    assert third_match.mid == poleng_match


def test_match_representation():
    """Test if matches are pretty-printable"""
    board = ScoreBoard()
    board.add("Poland", "England")
    poleng_match, = board.summary

    assert str(poleng_match) == "Poland 0 - England 0"

def test_match_representation_with_different_scores():
    """Test if match representation contains a valid score"""
    board = ScoreBoard()
    poleng_match = board.add("Poland", "England")
    board.update_score(poleng_match, 21, 37)

    poleng_match, = board.summary

    assert str(poleng_match) == "Poland 21 - England 37"

def test_empty_score_board_representation():
    """Test if emtpy score is pretty-printable"""
    board = ScoreBoard()

    assert str(board) == ''

def test_full_score_board_representation():
    """Test if full scoreboard is pretty-printable"""
    board = ScoreBoard()
    matches = [
        ("Mexico", 0, "Canada", 5),
        ("Spain", 10, "Brazil", 2),
        ("Germany", 2, "France", 2),
        ("Uruguay", 6, "Italy",  6),
        ("Argentina", 3, "Australia", 1)
    ]
    for (home_team, home_score, away_team, away_score) in matches:
        mid = board.add(home_team, away_team)
        board.update_score(mid, home_score, away_score)

    assert str(board) == (
    "1. Uruguay 6 - Italy 6\n"
    "2. Spain 10 - Brazil 2\n"
    "3. Mexico 0 - Canada 5\n"
    "4. Argentina 3 - Australia 1\n"
    "5. Germany 2 - France 2")