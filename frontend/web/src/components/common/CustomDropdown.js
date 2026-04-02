import { useState } from "react";
import { motion } from "framer-motion";

function CustomDropdown({ options, value, onChange, placeholder }) {
  const [open, setOpen] = useState(false);

  return (
    <div className="dropdown">

      {/* SELECT BOX */}
      <div
        className="dropdown-box"
        onClick={() => setOpen(!open)}
      >
        <span>
          {value
            ? options.find(o => o.value === value)?.label
            : placeholder}
        </span>
        <span>▼</span>
      </div>

      {/* DROPDOWN LIST */}
      {open && (
        <motion.div
          className="dropdown-list"
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
        >
          {options.map((opt) => (
            <div
              key={opt.value}
              className="dropdown-item"
              onClick={() => {
                onChange(opt.value);
                setOpen(false);
              }}
            >
              {opt.label}
            </div>
          ))}
        </motion.div>
      )}
    </div>
  );
}

export default CustomDropdown;