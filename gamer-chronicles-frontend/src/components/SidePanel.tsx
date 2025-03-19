import { useState } from "react";
import { Drawer, List, IconButton } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import DrawerList from "./DrawerList";

const SidePanel = () => {
  const [open, setOpen] = useState(false);

  return (
    <>
      <IconButton onClick={() => setOpen(true)} style={{ position: "absolute", top: 10, left: 10, zIndex: 1000 }}>
        <MenuIcon />
      </IconButton>
      <Drawer anchor="left" open={open} onClose={() => setOpen(false)}>
        <List>
            <DrawerList />
        </List>
      </Drawer>
    </>
  );
};

export default SidePanel;
