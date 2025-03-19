import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Container, TextField, Button, Typography, Box, Collapse } from "@mui/material";

const Login = () => {
  const [open, setOpen] = useState(true);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = () => {
    if (username === "admin" && password === "password") {
      localStorage.setItem("loggedIn", "true");
      navigate("/map");
    } else {
      alert("Invalid credentials");
    }
  };

  return (
    <Collapse in={open}>
      <Container maxWidth="xs">
        <Box mt={10} p={3} bgcolor="white" boxShadow={3} borderRadius={2}>
          <Typography variant="h5" mb={2}>Login</Typography>
          <TextField
            label="Username"
            variant="outlined"
            fullWidth
            margin="normal"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            label="Password"
            type="password"
            variant="outlined"
            fullWidth
            margin="normal"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <Button variant="contained" color="primary" fullWidth onClick={handleLogin}>
            Login
          </Button>
          <Button variant="text" fullWidth onClick={() => setOpen(false)}>
            Close
          </Button>
        </Box>
      </Container>
    </Collapse>
  );
};

export default Login;
