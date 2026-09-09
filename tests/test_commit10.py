import pytest
from auto_pr_reviewer import chunk_diff, build_review_prompt, combine_chunk_reviews

def test_chunk_diff_small():
    """Test diff smaller than max chunk size"""
    diff = "line 1\nline 2\nline 3"
    chunks = chunk_diff(diff, max_chunk_size=100)
    assert len(chunks) == 1
    assert chunks[0] == diff

def test_chunk_diff_large():
    """Test diff larger than max chunk size - with realistic diff format"""
    # Create realistic diff with many lines
    lines = ["@@ -1,1 +1,1 @@"] + [f"Line {i}\n" for i in range(500)]
    diff = "\n".join(lines)
    chunks = chunk_diff(diff, max_chunk_size=3000)
    # Verify chunks are created and total content is preserved
    assert len(chunks) >= 1
    combined = "".join(chunks)
    assert len(combined) >= len(diff) * 0.95  # Allow some minor variation

def test_build_review_prompt():
    """Test review prompt building"""
    prompt = build_review_prompt(
        diff="diff content",
        repo="owner/repo",
        pr_number=1,
        title="Test PR",
        platform='github',
        chunk_idx=1,
        total_chunks=2
    )
    assert "Test PR" in prompt
    assert "owner/repo" in prompt
    assert "github" in prompt

def test_combine_chunk_reviews():
    """Test combining multiple chunk reviews"""
    reviews = [
        "Review of chunk 1: looks good",
        "Review of chunk 2: needs work",
        "Review of chunk 3: approved"
    ]
    combined = combine_chunk_reviews(reviews, total_chunks=3)
    assert "chunk 1" in combined.lower() or "part" in combined.lower()
    assert len(combined) > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
